#!/usr/bin/env python3
"""
Enrich ANN report with UniProt annotations (gene names, Pfam, InterPro,
GO terms, taxonomic lineage, PDB structures) for queries and neighbors.
Generates markdown tables per algorithm; cells are bolded when the
neighbor shares the same annotation set as the query (gene/Pfam/
InterPro/GO/lineage).
"""

import argparse
import os
import re
import sys
from typing import Dict, List, Optional, Set, Tuple

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    print("requests is required. Install with: pip install requests")
    sys.exit(1)


Annotation = Dict[str, object]


def load_pfam_map(pfam_file: str) -> Dict[str, str]:
    """Load Pfam domain annotations from TSV file."""
    pfam_map = {}
    if not os.path.exists(pfam_file):
        return pfam_map
    
    with open(pfam_file, 'r') as f:
        next(f)  # Skip header
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                accession, pfam = parts[0], parts[1]
                pfam_map[accession] = pfam
    return pfam_map


def load_swissprot_map(fasta_file: str) -> Dict[str, str]:
    """Load SwissProt accession mapping from FASTA file.
    Maps plain accessions to sp|ACCESSION|NAME format.
    """
    swissprot_map = {}
    if not os.path.exists(fasta_file):
        return swissprot_map
    
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                # Format: >sp|Q7RY68|PFS2_NEUCR or >sp|ACCESSION|NAME
                parts = line[1:].split('|')
                if len(parts) >= 2 and parts[0] == 'sp':
                    accession = parts[1]
                    swissprot_map[accession] = True
    return swissprot_map


def make_session(retries: int = 3, backoff: float = 0.5, timeout: int = 10) -> requests.Session:
    """Create a requests session with retry logic."""
    session = requests.Session()
    retry = Retry(
        total=retries,
        backoff_factor=backoff,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.timeout = timeout
    return session


def fetch_uniprot(accession: str, session: requests.Session, is_swissprot: bool = False) -> Optional[Annotation]:
    """Fetch UniProt JSON and extract key annotations.
    If is_swissprot is True, the protein is from reviewed SwissProt database.
    """
    url = f"https://rest.uniprot.org/uniprotkb/{accession}.json"
    try:
        resp = session.get(url, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json()
        
        # Mark if this is a reviewed entry
        entry_type = data.get('entryType', 'Unknown')
        is_reviewed = entry_type == 'UniProtKB reviewed (Swiss-Prot)'
    except Exception:
        return None

    pfam: Set[str] = set()
    interpro: Set[str] = set()
    go_terms: Set[str] = set()
    gene3d: Set[str] = set()

    for ref in data.get("uniProtKBCrossReferences", []):
        db = ref.get("database")
        rid = ref.get("id")
        if db == "Pfam" and rid:
            pfam.add(rid)
        elif db == "InterPro" and rid:
            interpro.add(rid)
        elif db == "GO" and rid:
            # Get the GO term description from properties
            props = ref.get("properties", [])
            for prop in props:
                if prop.get("key") == "GoTerm":
                    term = prop.get("value")
                    if term:
                        go_terms.add(term)
        elif db == "Gene3D" and rid:
            gene3d.add(rid)

    lineage = data.get("organism", {}).get("lineage", []) or []
    organism = data.get("organism", {}).get("scientificName", "Unknown")

    return {
        "pfam": pfam,
        "interpro": interpro,
        "go": go_terms,
        "gene3d": gene3d,
        "lineage": lineage,
        "organism": organism,
        "reviewed": is_reviewed,
    }


def parse_report(report_path: str) -> Dict[str, Dict[str, List[Dict[str, str]]]]:
    """
    Parse results_with_bio.txt and return {method: {query: [neighbor rows]}}.
    Each neighbor row: {neighbor, blast_id, in_blast, distance}.
    """
    with open(report_path, "r") as f:
        content = f.read()

    methods: Dict[str, Dict[str, List[Dict[str, str]]]] = {}

    query_pattern = re.compile(r"Query:\s+([A-Za-z0-9_]+)")
    method_pattern = re.compile(r"Method:\s+(.+?)\nRank")
    row_pattern = re.compile(
        r"^\s*(\d+)\s+\|\s+([A-Za-z0-9_]+)\s+\|\s+([\d.]+)\s+\|\s+([^|]+?)\s+\|\s+([^|]+?)\s+\|",
        re.MULTILINE,
    )

    # Find query sections
    for q_match in query_pattern.finditer(content):
        query_id = q_match.group(1)
        start = q_match.end()
        next_q = query_pattern.search(content, start)
        end = next_q.start() if next_q else len(content)
        q_block = content[start:end]

        for m_match in method_pattern.finditer(q_block):
            method = m_match.group(1).strip()
            m_start = m_match.end()
            next_m = method_pattern.search(q_block, m_start)
            m_end = next_m.start() if next_m else len(q_block)
            m_block = q_block[m_start:m_end]

            for r_match in row_pattern.finditer(m_block):
                neighbor = r_match.group(2).strip()
                distance = r_match.group(3).strip()
                blast_id = r_match.group(4).strip()
                in_blast = r_match.group(5).strip()

                methods.setdefault(method, {}).setdefault(query_id, []).append(
                    {
                        "neighbor": neighbor,
                        "distance": distance,
                        "blast_id": blast_id,
                        "in_blast": in_blast,
                    }
                )

    return methods


def bold_if(text: str, condition: bool) -> str:
    if not text:
        return "-"
    return f"**{text}**" if condition else text


def bold_matching_items(items: Set[str], query_items: Set[str], limit: int = 5) -> str:
    """Bold only the items that match between sets, leave others plain."""
    if not items:
        return "-"
    
    sorted_items = sorted(items)
    if len(sorted_items) > limit:
        display_items = sorted_items[:limit]
        has_more = True
    else:
        display_items = sorted_items
        has_more = False
    
    formatted = []
    for item in display_items:
        if item in query_items:
            formatted.append(f"**{item}**")
        else:
            formatted.append(item)
    
    result = ", ".join(formatted)
    if has_more:
        result += ", …"
    return result


def join_set(values: Set[str], limit: int = 5) -> str:
    if not values:
        return "-"
    items = sorted(values)
    if len(items) > limit:
        items = items[:limit] + ["…"]
    return ", ".join(items)


def lineage_str(lineage: List[str]) -> str:
    return " > ".join(lineage) if lineage else "-"


def get_common_neighbors(methods: Dict[str, Dict[str, List[Dict[str, str]]]], query_id: str) -> tuple:
    """Find neighbors that appear in all methods and 4+ methods for a given query.
    Returns: (all_5_methods, four_or_more_methods) sets"""
    neighbor_counts: Dict[str, int] = {}
    num_methods = 0
    
    for method, queries in methods.items():
        if query_id in queries:
            num_methods += 1
            for entry in queries[query_id]:
                neighbor = entry["neighbor"]
                neighbor_counts[neighbor] = neighbor_counts.get(neighbor, 0) + 1
    
    if num_methods == 0:
        return set(), set()
    
    all_5 = {neighbor for neighbor, count in neighbor_counts.items() if count == num_methods}
    four_or_more = {neighbor for neighbor, count in neighbor_counts.items() if count >= 4}
    return all_5, four_or_more


def build_tables(methods: Dict[str, Dict[str, List[Dict[str, str]]]], out_path: str, session: requests.Session, pfam_map: Dict[str, str], swissprot_map: Dict[str, bool]) -> None:
    cache: Dict[str, Optional[Annotation]] = {}

    lines: List[str] = []
    lines.append("# Annotation Enrichment Report\n")
    lines.append("## Glossary\n")
    lines.append("- **Pfam**: Protein family domains (from UniProt and local mapping file)")
    lines.append("- **InterPro**: Integrated protein signature database")
    lines.append("- **GO**: Gene Ontology terms - biological function, cellular component, molecular process")
    lines.append("- **Gene3D**: Structural domain classification in CATH hierarchy (format: a.b.c.d)")
    lines.append("- **Lineage**: Taxonomic classification from kingdom to species")
    lines.append("- **Neighbor Protein Formatting**: ")
    lines.append("  - **Bold**: Neighbors appearing in ALL 5 search methods (most reliable)")
    lines.append("  - <u>Underlined</u>: Neighbors appearing in 4 out of 5 methods (highly reliable)")
    lines.append("  - Normal: Neighbors from fewer methods")
    lines.append(f"\n**Note**: Using SwissProt (reviewed) entries when available. Found {len(swissprot_map)} SwissProt proteins in database.\n")

    for method, queries in methods.items():
        lines.append(f"\n## {method}\n")
        for query_id, rows in queries.items():
            # Get neighbors that appear in all methods and 4+ methods for this query
            common_neighbors_all_5, common_neighbors_4plus = get_common_neighbors(methods, query_id)
            
            # Fetch query annotation
            if query_id not in cache:
                is_sp = query_id in swissprot_map
                cache[query_id] = fetch_uniprot(query_id, session, is_sp)
            q_ann = cache[query_id]

            # Get query Pfam from local file
            q_pfam_local = pfam_map.get(query_id, "")
            q_pfam = q_ann.get("pfam", set()) if q_ann else set()
            if q_pfam_local and not q_pfam:
                q_pfam = {q_pfam_local}
            
            lines.append(f"\n### Query: {query_id}\n")
            
            # Add query information
            q_ipr = q_ann.get("interpro", set()) if q_ann else set()
            q_go = q_ann.get("go", set()) if q_ann else set()
            q_lin = q_ann.get("lineage", []) if q_ann else []
            q_gene3d = q_ann.get("gene3d", set()) if q_ann else set()
            q_organism = q_ann.get("organism", "Unknown") if q_ann else "Unknown"
            
            lines.append("**Query Information:**")
            lines.append(f"- **Organism**: {q_organism}")
            lines.append(f"- **Pfam Domain**: {', '.join(sorted(q_pfam)) if q_pfam else 'None found'}")
            lines.append(f"- **InterPro**: {', '.join(sorted(q_ipr)) if q_ipr else 'None found'}")
            lines.append(f"- **GO Terms**: {join_set(q_go) if q_go else 'None found'}")
            lines.append(f"- **Gene3D**: {', '.join(sorted(q_gene3d)) if q_gene3d else 'None found'}")
            lines.append(f"- **Lineage**: {lineage_str(q_lin) if q_lin else 'None found'}")
            lines.append("")

            q_lin_set = set(q_lin)

            lines.append("**Neighbor Annotations:**\n")
            lines.append("| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |")
            lines.append("|---|---|---|---|---|---|---|---|")

            for entry in rows:
                nb = entry["neighbor"]
                # Bold neighbor name if it appears in all 5 methods, underline if 4+ methods
                if nb in common_neighbors_all_5:
                    neighbor_display = f"**{nb}**"
                elif nb in common_neighbors_4plus:
                    neighbor_display = f"<u>{nb}</u>"
                else:
                    neighbor_display = nb
                
                if nb not in cache:
                    is_sp = nb in swissprot_map
                    cache[nb] = fetch_uniprot(nb, session, is_sp)
                n_ann = cache[nb]

                # Get neighbor Pfam from local file
                n_pfam_local = pfam_map.get(nb, "")
                n_pfam = n_ann.get("pfam", set()) if n_ann else set()
                if n_pfam_local and not n_pfam:
                    n_pfam = {n_pfam_local}

                n_ipr = n_ann.get("interpro", set()) if n_ann else set()
                n_go = n_ann.get("go", set()) if n_ann else set()
                n_lin = n_ann.get("lineage", []) if n_ann else []
                n_lin_set = set(n_lin)
                n_gene3d = n_ann.get("gene3d", set()) if n_ann else set()

                pfam_match = bool(q_pfam & n_pfam)
                ipr_match = bool(q_ipr & n_ipr)
                go_match = bool(q_go & n_go)
                gene3d_match = bool(q_gene3d & n_gene3d)
                lin_match = bool(q_lin_set & n_lin_set)

                # Bold only matching individual items
                pfam_str = bold_matching_items(n_pfam, q_pfam)
                ipr_str = bold_matching_items(n_ipr, q_ipr)
                go_str = bold_matching_items(n_go, q_go)
                gene3d_str = bold_matching_items(n_gene3d, q_gene3d)
                
                # For lineage, bold only matching taxonomic terms
                if n_lin:
                    lin_parts = [f"**{term}**" if term in q_lin_set else term for term in n_lin]
                    lin_str = " > ".join(lin_parts)
                else:
                    lin_str = "-"

                lines.append(
                    "| {neighbor} | {blast} | {in_blast} | {pfam} | {ipr} | {go} | {gene3d} | {lin} |".format(
                        neighbor=neighbor_display,
                        blast=entry["blast_id"],
                        in_blast=entry["in_blast"],
                        pfam=pfam_str,
                        ipr=ipr_str,
                        go=go_str,
                        gene3d=gene3d_str,
                        lin=lin_str,
                    )
                )
            lines.append("")

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description="Enrich ANN report with UniProt annotations.")
    parser.add_argument("-i", "--input", required=True, help="Path to results_with_bio.txt")
    parser.add_argument("-o", "--output", required=True, help="Path to output markdown file")
    parser.add_argument("-p", "--pfam", default="Data/targets.pfam_map.tsv", help="Path to Pfam mapping TSV file")
    parser.add_argument("-s", "--swissprot", default="Data/swissprot_50k.fasta", help="Path to SwissProt FASTA file")
    args = parser.parse_args()

    methods = parse_report(args.input)
    if not methods:
        print("No methods/queries parsed; check input format.")
        return

    # Load local Pfam annotations
    pfam_map = load_pfam_map(args.pfam)
    if pfam_map:
        print(f"Loaded Pfam annotations for {len(pfam_map)} proteins")
    else:
        print("Warning: No local Pfam annotations loaded")
    
    # Load SwissProt proteins
    swissprot_map = load_swissprot_map(args.swissprot)
    if swissprot_map:
        print(f"Loaded {len(swissprot_map)} SwissProt (reviewed) proteins")
    else:
        print("Warning: No SwissProt database loaded")

    session = make_session()
    build_tables(methods, args.output, session, pfam_map, swissprot_map)
    print(f"Annotation report written to {args.output}")


if __name__ == "__main__":
    main()
