# Annotation Enrichment Report - README

## What was fixed

The annotation enrichment report had several issues that have now been resolved:

### 1. **Query Information Added**
Previously, the report only showed neighbor information without any context about the query protein itself. Now, each query section includes:
- **Organism**: The species the protein comes from
- **Genes**: Gene names (if available)
- **Pfam Domain**: Protein family classification from local data
- **InterPro**: Integrated protein signatures (from UniProt API)
- **GO Terms**: Gene Ontology functional annotations (from UniProt API)
- **Lineage**: Complete taxonomic classification
- **PDB Structures**: 3D structure identifiers if available

### 2. **Pfam Domains Now Populated**
The Pfam column was empty because the UniProt API doesn't return this data for most TrEMBL (unreviewed) proteins. The script now:
- Loads Pfam domain annotations from the local file `Data/targets.pfam_map.tsv`
- Uses this data to populate the Pfam column for both queries and neighbors
- Shows matching domains in **bold** when neighbors share the same Pfam domain as the query

### 3. **Glossary Added**
A glossary section at the top now explains what each column means:
- **Genes**: Gene names associated with the protein
- **Pfam**: Protein family domains (from local mapping file)
- **InterPro**: Integrated protein signature database (from UniProt)
- **GO**: Gene Ontology terms describing biological function (from UniProt)
- **Lineage**: Taxonomic classification
- **PDB**: Protein Data Bank 3D structure identifiers (if protein structure is available)

### 4. **Clear Note About Data Availability**
The report now includes a note explaining that most proteins are from TrEMBL (unreviewed entries) and therefore lack detailed annotations like InterPro, GO terms, and PDB structures.

## Why are InterPro, GO, and PDB still empty?

These columns remain empty because:

1. **TrEMBL vs SwissProt**: Most proteins in this analysis are from TrEMBL (unreviewed), not SwissProt (manually curated). TrEMBL entries typically have minimal annotations.

2. **Limited UniProt Data**: The UniProt API simply doesn't return these fields for most of these proteins. They haven't been experimentally characterized or manually annotated.

3. **Pfam is Different**: Pfam domains can be predicted computationally from sequence alone, which is why we have local Pfam data even for unreviewed proteins.

## Example of Improvements

### Before:
```
### Query: A0A009HQC9

| Neighbor | Blast ID | In BLAST? | Genes | Pfam | InterPro | GO | Lineage | PDB |
|---|---|---|---|---|---|---|---|---|
| Q0HR19 | 45% | Yes | **rapA** | - | - | - | ... | - |
```

### After:
```
### Query: A0A009HQC9

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Genes**: rapA
- **Pfam Domain**: PF00271
- **InterPro**: None found
- **GO Terms**: None found
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > ...
- **PDB Structures**: None available

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Genes | Pfam | InterPro | GO | Lineage | PDB |
|---|---|---|---|---|---|---|---|---|
| Q0HR19 | 45% | Yes | **rapA** | - | - | - | ... | - |
```

## How to regenerate the report

If you need to regenerate the report:

```bash
cd /home/marialtr/project_part3/Part3
python3 src/enrich_annotations.py \
    -i output/search/results_with_bio.txt \
    -o output/evaluation/annotation_enrichment.md \
    -p Data/targets.pfam_map.tsv
```

## Understanding the bold formatting

In the neighbor tables, annotations are shown in **bold** when they match the query's annotations:
- **Bold gene names**: The neighbor shares at least one gene name with the query
- **Bold Pfam**: The neighbor has the same Pfam domain as the query
- **Bold lineage terms**: The neighbor shares taxonomic classification with the query

This helps identify functionally similar proteins at a glance.
