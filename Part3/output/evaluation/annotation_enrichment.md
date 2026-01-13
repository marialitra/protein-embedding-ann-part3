# Annotation Enrichment Report

## Glossary

- **Pfam**: Protein family domains (from UniProt and local mapping file)
- **InterPro**: Integrated protein signature database
- **GO**: Gene Ontology terms - biological function, cellular component, molecular process
- **Gene3D**: Structural domain classification in CATH hierarchy (format: a.b.c.d)
- **Lineage**: Taxonomic classification from kingdom to species
- **Neighbor Protein Formatting**: 
  - **Bold**: Neighbors appearing in ALL 5 search methods (most reliable)
  - <u>Underlined</u>: Neighbors appearing in 4 out of 5 methods (highly reliable)
  - Normal: Neighbors from fewer methods

**Note**: Using SwissProt (reviewed) entries when available. Found 50000 SwissProt proteins in database.


## Euclidean LSH


### Query: A0A009PCK4

**Query Information:**
- **Organism**: Acinetobacter baumannii 625974
- **Pfam Domain**: PF00069
- **InterPro**: IPR000719, IPR011009
- **GO Terms**: F:ATP binding, F:protein serine/threonine kinase activity
- **Gene3D**: 1.10.510.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>⭐)A5UG81</u> | undetected | No | PF06293 | **IPR011009**, IPR022826 | C:plasma membrane, **F:ATP binding**, F:kinase activity, F:phosphotransferase activity, alcohol group as acceptor, P:lipopolysaccharide core region biosynthetic process | **1.10.510.10** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P44033</u> | undetected | No | PF07804 | IPR012893, IPR052028 | C:cytosol, **F:protein serine/threonine kinase activity** | 1.10.1070.20 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P14181</u> | undetected | No | PF01633 | **IPR011009**, IPR052077 | - | 3.30.200.20, 3.90.1200.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| ⭐)Q8EKA0 | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| <u>B2K7I7</u> | undetected | No | PF12592, PF17868, PF20030, PF20265 | IPR003593, IPR022547, IPR023671, IPR027417, IPR041538, … | C:cytoplasm, **F:ATP binding**, F:ATP hydrolysis activity | 1.20.58.1510, 2.40.128.430, 3.40.50.300 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Yersiniaceae > Yersinia |
| Q12SQ2 | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| <u>A1SW96</u> | undetected | No | PF01266, PF05430 | IPR006076, IPR008471, IPR017610, IPR023032, IPR029063, … | C:cytoplasm, F:flavin adenine dinucleotide binding, F:oxidoreductase activity, acting on the CH-NH group of donors, F:tRNA (5-methylaminomethyl-2-thiouridylate)(34)-methyltransferase activity, P:methylation, … | 3.30.9.10, 3.40.50.150, 3.50.50.60 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Psychromonadaceae > Psychromonas |
| <u>B4F0D4</u> | undetected | No | PF05762 | IPR002035, IPR008912, IPR023481, IPR036465 | C:cytosol | 3.40.50.410 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Morganellaceae > Proteus |
| <u>A3DA85</u> | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| <u>Q4QLU9</u> | undetected | No | PF05958 | IPR010280, IPR011825, IPR029063, IPR030390, IPR030391 | F:4 iron, 4 sulfur cluster binding, F:iron ion binding, F:rRNA (uridine-C5-)-methyltransferase activity, P:rRNA base methylation | 2.40.50.1070, 3.40.50.150 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |


### Query: A0A002

**Query Information:**
- **Organism**: Streptomyces viridosporus
- **Pfam Domain**: PF00005, PF00664
- **InterPro**: IPR003439, IPR003593, IPR011527, IPR027417, IPR036640, IPR039421
- **GO Terms**: C:plasma membrane, F:ABC-type transporter activity, F:ATP binding, F:ATP hydrolysis activity
- **Gene3D**: 1.20.1560.10, 3.40.50.300
- **Lineage**: Bacteria > Bacillati > Actinomycetota > Actinomycetes > Kitasatosporales > Streptomycetaceae > Streptomyces

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>⭐)P9WQJ3</u> | 28% | Yes | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled transmembrane transporter activity, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > Mycobacteriales > Mycobacteriaceae > Mycobacterium > Mycobacterium tuberculosis complex |
| <u>Q13BH6</u> | 29% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, F:ABC-type beta-glucan transporter activity, F:ABC-type oligopeptide transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Alphaproteobacteria > Hyphomicrobiales > Nitrobacteraceae > Rhodopseudomonas |
| <u>Q03024</u> | 31% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, IPR010128, **IPR011527**, IPR017871, … | **C:plasma membrane**, C:type I protein secretion system complex, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Pseudomonadales > Pseudomonadaceae > Pseudomonas |
| <u>Q20Z38</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, F:ABC-type beta-glucan transporter activity, F:ABC-type oligopeptide transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Alphaproteobacteria > Hyphomicrobiales > Nitrobacteraceae > Rhodopseudomonas |
| <u>P23886</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR014223, IPR017871, … | C:ATP-binding cassette (ABC) transporter complex, C:ATP-binding cassette (ABC) transporter complex, integrated substrate binding, **C:plasma membrane**, F:ABC-type heme transporter activity, **F:ATP binding**, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Enterobacterales > Enterobacteriaceae > Escherichia |
| <u>Q8P8W4</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR011917, IPR017871, … | **C:plasma membrane**, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled lipid transmembrane transporter activity, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Lysobacterales > Lysobacteraceae > Xanthomonas |
| Q51719 | 31% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR005876, IPR015856, **IPR027417**, … | C:ATP-binding cassette (ABC) transporter complex, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled transmembrane transporter activity, P:cobalt ion transport | **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > Propionibacteriales > Propionibacteriaceae > Propionibacterium |
| Q82MV1 | 30% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR017871, **IPR027417**, IPR050166 | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > **Kitasatosporales** > **Streptomycetaceae** > **Streptomyces** |
| <u>Q28433</u> | 27% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR013305, IPR017871, … | C:MHC class I peptide loading complex, C:membrane, F:ABC-type peptide antigen transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity**, … | **1.20.1560.10**, **3.40.50.300** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Euarchontoglires > Primates > Haplorrhini > Catarrhini > Hominidae > Gorilla |
| <u>A0K739</u> | 33% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR017871, **IPR027417**, IPR050166 | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Betaproteobacteria > Burkholderiales > Burkholderiaceae > Burkholderia > Burkholderia cepacia complex |


### Query: A0A009HN45

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR027417, IPR038718, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:helicase activity, F:hydrolase activity
- **Gene3D**: 3.40.50.10810, 3.40.50.300
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>A6QKD8</u> | undetected | No | PF01043, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:protein-exporting ATPase activity, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Staphylococcaceae > Staphylococcus |
| **A7MSB2** | 36% | Yes | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| <u>Q3K063</u> | undetected | No | PF01043, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:protein-exporting ATPase activity, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| **⭐)Q9ZDW2** | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > Alphaproteobacteria > Rickettsiales > Rickettsiaceae > Rickettsieae > Rickettsia > typhus group |
| <u>Q1MQP3</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR004027, IPR011115, IPR011116, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > Thermodesulfobacteriota > Desulfovibrionia > Desulfovibrionales > Desulfovibrionaceae > Lawsonia |
| <u>Q7VJC6</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR004027, IPR011115, IPR011116, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > Campylobacterota > Epsilonproteobacteria > Campylobacterales > Helicobacteraceae > Helicobacter |
| <u>B0BT63</u> | 34% | Yes | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Actinobacillus |
| <u>Q92H92</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, IPR004027, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > Alphaproteobacteria > Rickettsiales > Rickettsiaceae > Rickettsieae > Rickettsia > spotted fever group |
| **P52126** | undetected | No | PF00270, **PF00271** | **IPR001650**, IPR011545, **IPR014001**, **IPR027417**, IPR050699 | **F:ATP binding**, **F:helicase activity**, **F:hydrolase activity**, F:nucleic acid binding, P:defense response to virus, … | **3.40.50.300** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| <u>Q0HMR2</u> | 30% | No | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |


### Query: A0A009HQC9

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271, PF12137, PF18337, PF18339
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR022737, IPR023949, IPR027417, IPR038718, IPR040765, IPR040766, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:DNA binding, F:helicase activity, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription
- **Gene3D**: 2.30.30.140, 2.30.30.930, 3.30.360.80, 3.40.50.10810, 3.40.50.300, 6.10.140.1500
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **⭐)Q0HR19** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **Q0HMR2** | 44% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **A0KGL5** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Aeromonadales > Aeromonadaceae > Aeromonas |
| **A1A7A6** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **A7ZW09** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **B0BT63** | 40% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Actinobacillus |
| **A7MSB2** | 44% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| <u>Q48LP5</u> | 44% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Pseudomonas |
| **B5FI41** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |
| **Q5PDF0** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |


### Query: A0A009IB02

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00198, PF00364, PF02817
- **InterPro**: IPR000089, IPR001078, IPR003016, IPR004167, IPR011053, IPR023213, IPR036625, IPR050743
- **GO Terms**: C:cytoplasm, F:dihydrolipoyllysine-residue acetyltransferase activity, F:lipoic acid binding, P:pyruvate decarboxylation to acetyl-CoA
- **Gene3D**: 2.40.50.100, 3.30.559.10, 4.10.320.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **P10802** | 46% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, IPR006256, … | **C:cytoplasm**, C:pyruvate dehydrogenase complex, **F:dihydrolipoyllysine-residue acetyltransferase activity**, **F:lipoic acid binding**, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Azotobacter |
| <u>P11961</u> | 38% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | **C:cytoplasm**, **F:dihydrolipoyllysine-residue acetyltransferase activity**, **F:lipoic acid binding** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Anoxybacillaceae > Geobacillus |
| <u>Q9SQI8</u> | 42% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | C:chloroplast, C:chloroplast envelope, C:chloroplast stroma, C:chloroplast thylakoid, C:cytosol, … | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | Eukaryota > Viridiplantae > Streptophyta > Embryophyta > Tracheophyta > Spermatophyta > Magnoliopsida > eudicotyledons > Gunneridae > Pentapetalae > rosids > malvids > Brassicales > Brassicaceae > Camelineae > Arabidopsis |
| <u>P49786</u> | undetected | No | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Bacillaceae > Bacillus |
| **P22439** | 26% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | C:mitochondrial matrix, C:mitochondrion, C:pyruvate dehydrogenase complex, F:acyltransferase activity, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Laurasiatheria > Artiodactyla > Ruminantia > Pecora > Bovidae > Bovinae > Bos |
| <u>P43874</u> | 41% | Yes | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P29337</u> | 41% | Yes | **PF00364** | **IPR000089**, IPR001882, **IPR011053**, IPR050709 | P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| <u>P02904</u> | 40% | Yes | **PF00364** | **IPR000089**, IPR001882, **IPR011053**, IPR050709 | F:methylmalonyl-CoA carboxytransferase activity | **2.40.50.100** | **Bacteria** > Bacillati > Actinomycetota > Actinomycetes > Propionibacteriales > Propionibacteriaceae > Propionibacterium |
| <u>Q06881</u> | 32% | Yes | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR053217 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Cyanobacteriota > Cyanophyceae > Nostocales > Nostocaceae > Nostoc |
| <u>P0ABE1</u> | 36% | No | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Shigella |


## Hypercube


### Query: A0A009PCK4

**Query Information:**
- **Organism**: Acinetobacter baumannii 625974
- **Pfam Domain**: PF00069
- **InterPro**: IPR000719, IPR011009
- **GO Terms**: F:ATP binding, F:protein serine/threonine kinase activity
- **Gene3D**: 1.10.510.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>B2K7I7</u> | undetected | No | PF12592, PF17868, PF20030, PF20265 | IPR003593, IPR022547, IPR023671, IPR027417, IPR041538, … | C:cytoplasm, **F:ATP binding**, F:ATP hydrolysis activity | 1.20.58.1510, 2.40.128.430, 3.40.50.300 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Yersiniaceae > Yersinia |
| <u>A1SW96</u> | undetected | No | PF01266, PF05430 | IPR006076, IPR008471, IPR017610, IPR023032, IPR029063, … | C:cytoplasm, F:flavin adenine dinucleotide binding, F:oxidoreductase activity, acting on the CH-NH group of donors, F:tRNA (5-methylaminomethyl-2-thiouridylate)(34)-methyltransferase activity, P:methylation, … | 3.30.9.10, 3.40.50.150, 3.50.50.60 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Psychromonadaceae > Psychromonas |
| <u>B4F0D4</u> | undetected | No | PF05762 | IPR002035, IPR008912, IPR023481, IPR036465 | C:cytosol | 3.40.50.410 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Morganellaceae > Proteus |
| Q8EJX6 | undetected | No | PF02696 | IPR003846 | F:AMPylase activity, **F:ATP binding**, F:magnesium ion binding | - | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| A1RPL0 | undetected | No | PF02696 | IPR003846 | F:AMPylase activity, **F:ATP binding**, F:magnesium ion binding | - | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| P47448 | undetected | No | PF01541, PF08459, PF12826, PF22920 | IPR000305, IPR001162, IPR004791, IPR010994, IPR035901, … | C:cytoplasm, C:excinuclease repair complex, F:DNA binding, F:excinuclease ABC activity, P:DNA damage response, … | 1.10.150.20, 3.30.420.340, 3.40.1440.10 | **Bacteria** > Bacillati > Mycoplasmatota > Mycoplasmoidales > Mycoplasmoidaceae > Mycoplasmoides |
| A0L1Z0 | undetected | No | PF02696 | IPR003846 | F:AMPylase activity, **F:ATP binding**, F:magnesium ion binding | - | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| Q9CP74 | undetected | No | PF00575, PF00773, PF08206 | IPR001900, IPR003029, IPR004476, IPR011129, IPR011804, … | C:cytosol, F:RNA binding, F:exoribonuclease II activity, P:mRNA catabolic process | 2.40.50.140, 2.40.50.640 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Pasteurella |
| A9KYL6 | undetected | No | PF03109 | IPR004147, IPR010232, **IPR011009**, IPR045308, IPR050154 | C:plasma membrane, **F:ATP binding**, F:protein kinase activity, P:regulation of ubiquinone biosynthetic process, P:ubiquinone biosynthetic process | - | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| O74738 | undetected | No | - | IPR001214, IPR011219, IPR036464, IPR044432, IPR046341, … | C:cytosol, C:nucleus, F:protein-lysine N-methyltransferase activity, P:methylation, P:ribosome biogenesis | 3.90.1410.10, 3.90.1420.10 | Eukaryota > Fungi > Dikarya > Ascomycota > Taphrinomycotina > Schizosaccharomycetes > Schizosaccharomycetales > Schizosaccharomycetaceae > Schizosaccharomyces |


### Query: A0A002

**Query Information:**
- **Organism**: Streptomyces viridosporus
- **Pfam Domain**: PF00005, PF00664
- **InterPro**: IPR003439, IPR003593, IPR011527, IPR027417, IPR036640, IPR039421
- **GO Terms**: C:plasma membrane, F:ABC-type transporter activity, F:ATP binding, F:ATP hydrolysis activity
- **Gene3D**: 1.20.1560.10, 3.40.50.300
- **Lineage**: Bacteria > Bacillati > Actinomycetota > Actinomycetes > Kitasatosporales > Streptomycetaceae > Streptomyces

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>P9WQJ3</u> | 28% | Yes | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled transmembrane transporter activity, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > Mycobacteriales > Mycobacteriaceae > Mycobacterium > Mycobacterium tuberculosis complex |
| <u>Q13BH6</u> | 29% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, F:ABC-type beta-glucan transporter activity, F:ABC-type oligopeptide transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Alphaproteobacteria > Hyphomicrobiales > Nitrobacteraceae > Rhodopseudomonas |
| <u>Q03024</u> | 31% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, IPR010128, **IPR011527**, IPR017871, … | **C:plasma membrane**, C:type I protein secretion system complex, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Pseudomonadales > Pseudomonadaceae > Pseudomonas |
| <u>Q20Z38</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, F:ABC-type beta-glucan transporter activity, F:ABC-type oligopeptide transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Alphaproteobacteria > Hyphomicrobiales > Nitrobacteraceae > Rhodopseudomonas |
| <u>P23886</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR014223, IPR017871, … | C:ATP-binding cassette (ABC) transporter complex, C:ATP-binding cassette (ABC) transporter complex, integrated substrate binding, **C:plasma membrane**, F:ABC-type heme transporter activity, **F:ATP binding**, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Enterobacterales > Enterobacteriaceae > Escherichia |
| <u>Q8P8W4</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR011917, IPR017871, … | **C:plasma membrane**, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled lipid transmembrane transporter activity, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Lysobacterales > Lysobacteraceae > Xanthomonas |
| <u>Q28433</u> | 27% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR013305, IPR017871, … | C:MHC class I peptide loading complex, C:membrane, F:ABC-type peptide antigen transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity**, … | **1.20.1560.10**, **3.40.50.300** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Euarchontoglires > Primates > Haplorrhini > Catarrhini > Hominidae > Gorilla |
| O70595 | 32% | No | **PF00005**, **PF00664**, PF16185 | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | C:Golgi apparatus, C:Golgi membrane, C:cytosol, C:early endosome membrane, C:endolysosome membrane, … | **1.20.1560.10**, **3.40.50.300** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Euarchontoglires > Glires > Rodentia > Myomorpha > Muroidea > Muridae > Murinae > Rattus |
| Q9NP58 | 32% | No | **PF00005**, **PF00664**, PF16185 | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | C:ATP-binding cassette (ABC) transporter complex, C:Golgi apparatus, C:Golgi membrane, C:cytosol, C:early endosome membrane, … | **1.20.1560.10**, **3.40.50.300** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Euarchontoglires > Primates > Haplorrhini > Catarrhini > Hominidae > Homo |
| P9WQJ4 | 27% | No | **PF00005**, PF08352 | **IPR003439**, **IPR003593**, IPR013563, IPR017871, **IPR027417**, … | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity**, P:peptide transport | **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > Mycobacteriales > Mycobacteriaceae > Mycobacterium > Mycobacterium tuberculosis complex |


### Query: A0A009HN45

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR027417, IPR038718, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:helicase activity, F:hydrolase activity
- **Gene3D**: 3.40.50.10810, 3.40.50.300
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>A6QKD8</u> | undetected | No | PF01043, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:protein-exporting ATPase activity, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Staphylococcaceae > Staphylococcus |
| **A7MSB2** | 36% | Yes | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| <u>Q3K063</u> | undetected | No | PF01043, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:protein-exporting ATPase activity, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| **Q9ZDW2** | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > Alphaproteobacteria > Rickettsiales > Rickettsiaceae > Rickettsieae > Rickettsia > typhus group |
| <u>Q1MQP3</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR004027, IPR011115, IPR011116, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > Thermodesulfobacteriota > Desulfovibrionia > Desulfovibrionales > Desulfovibrionaceae > Lawsonia |
| <u>Q7VJC6</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR004027, IPR011115, IPR011116, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > Campylobacterota > Epsilonproteobacteria > Campylobacterales > Helicobacteraceae > Helicobacter |
| <u>B0BT63</u> | 34% | Yes | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Actinobacillus |
| <u>Q92H92</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, IPR004027, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > Alphaproteobacteria > Rickettsiales > Rickettsiaceae > Rickettsieae > Rickettsia > spotted fever group |
| **P52126** | undetected | No | PF00270, **PF00271** | **IPR001650**, IPR011545, **IPR014001**, **IPR027417**, IPR050699 | **F:ATP binding**, **F:helicase activity**, **F:hydrolase activity**, F:nucleic acid binding, P:defense response to virus, … | **3.40.50.300** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| <u>Q0HMR2</u> | 30% | No | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |


### Query: A0A009HQC9

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271, PF12137, PF18337, PF18339
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR022737, IPR023949, IPR027417, IPR038718, IPR040765, IPR040766, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:DNA binding, F:helicase activity, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription
- **Gene3D**: 2.30.30.140, 2.30.30.930, 3.30.360.80, 3.40.50.10810, 3.40.50.300, 6.10.140.1500
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **Q0HR19** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **Q0HMR2** | 44% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **A0KGL5** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Aeromonadales > Aeromonadaceae > Aeromonas |
| **A1A7A6** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **A7ZW09** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **B0BT63** | 40% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Actinobacillus |
| **A7MSB2** | 44% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| <u>Q48LP5</u> | 44% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Pseudomonas |
| **B5FI41** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |
| **Q5PDF0** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |


### Query: A0A009IB02

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00198, PF00364, PF02817
- **InterPro**: IPR000089, IPR001078, IPR003016, IPR004167, IPR011053, IPR023213, IPR036625, IPR050743
- **GO Terms**: C:cytoplasm, F:dihydrolipoyllysine-residue acetyltransferase activity, F:lipoic acid binding, P:pyruvate decarboxylation to acetyl-CoA
- **Gene3D**: 2.40.50.100, 3.30.559.10, 4.10.320.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **P10802** | 46% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, IPR006256, … | **C:cytoplasm**, C:pyruvate dehydrogenase complex, **F:dihydrolipoyllysine-residue acetyltransferase activity**, **F:lipoic acid binding**, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Azotobacter |
| <u>Q9SQI8</u> | 42% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | C:chloroplast, C:chloroplast envelope, C:chloroplast stroma, C:chloroplast thylakoid, C:cytosol, … | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | Eukaryota > Viridiplantae > Streptophyta > Embryophyta > Tracheophyta > Spermatophyta > Magnoliopsida > eudicotyledons > Gunneridae > Pentapetalae > rosids > malvids > Brassicales > Brassicaceae > Camelineae > Arabidopsis |
| **P22439** | 26% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | C:mitochondrial matrix, C:mitochondrion, C:pyruvate dehydrogenase complex, F:acyltransferase activity, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Laurasiatheria > Artiodactyla > Ruminantia > Pecora > Bovidae > Bovinae > Bos |
| Q6MMS6 | undetected | No | PF00009, PF03144, PF04760, PF11987, PF22042 | IPR000178, IPR000795, IPR004161, IPR005225, IPR006847, … | C:cytosol, F:GTP binding, F:GTPase activity, F:translation initiation factor activity | 1.10.10.2480, 2.40.30.10, 3.40.50.10050, 3.40.50.300 | **Bacteria** > **Pseudomonadati** > Bdellovibrionota > Bdellovibrionia > Bdellovibrionales > Pseudobdellovibrionaceae > Bdellovibrio |
| B5XWP9 | undetected | No | PF01512, PF10531, PF12838, PF13375 | IPR010208, IPR011538, IPR017896, IPR017900, IPR019554, … | C:plasma membrane, F:4 iron, 4 sulfur cluster binding, F:electron transfer activity, F:metal ion binding, P:electron transport chain | 3.30.70.20, 3.40.50.11540 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Klebsiella/Raoultella group > Klebsiella > Klebsiella pneumoniae complex |
| A9N025 | undetected | No | PF01512, PF10531, PF12838, PF13375 | IPR010208, IPR011538, IPR017896, IPR017900, IPR019554, … | C:plasma membrane, F:4 iron, 4 sulfur cluster binding, F:electron transfer activity, F:metal ion binding, P:electron transport chain | 3.30.70.20, 3.40.50.11540 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |
| A8AH10 | undetected | No | PF01512, PF10531, PF12838, PF13375 | IPR010208, IPR011538, IPR017896, IPR017900, IPR019554, … | C:plasma membrane, F:4 iron, 4 sulfur cluster binding, F:electron transfer activity, F:metal ion binding, P:electron transport chain | 3.30.70.20, 3.40.50.11540 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Citrobacter |
| C6DH15 | undetected | No | PF01512, PF10531, PF12838, PF13375 | IPR010208, IPR011538, IPR017896, IPR017900, IPR019554, … | C:plasma membrane, F:4 iron, 4 sulfur cluster binding, F:electron transfer activity, F:metal ion binding, P:electron transport chain | 3.30.70.20, 3.40.50.11540 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Pectobacteriaceae > Pectobacterium |
| Q56WK6 | undetected | No | PF00650, PF03765, PF25099 | IPR001251, IPR009038, IPR011074, IPR036273, IPR036598, … | C:Golgi apparatus, C:apoplast, C:mitochondrion, C:plasma membrane, C:plasmodesma, … | 1.10.8.20, 2.60.120.680, 3.40.525.10 | Eukaryota > Viridiplantae > Streptophyta > Embryophyta > Tracheophyta > Spermatophyta > Magnoliopsida > eudicotyledons > Gunneridae > Pentapetalae > rosids > malvids > Brassicales > Brassicaceae > Camelineae > Arabidopsis |
| Q56ZI2 | undetected | No | PF00650, PF03765, PF25099 | IPR001251, IPR009038, IPR011074, IPR036273, IPR036598, … | C:Golgi apparatus, C:nucleus, C:plasma membrane, F:lipid binding, F:protease binding, … | 2.60.120.680, 3.40.525.10 | Eukaryota > Viridiplantae > Streptophyta > Embryophyta > Tracheophyta > Spermatophyta > Magnoliopsida > eudicotyledons > Gunneridae > Pentapetalae > rosids > malvids > Brassicales > Brassicaceae > Camelineae > Arabidopsis |


## IVF-Flat


### Query: A0A009PCK4

**Query Information:**
- **Organism**: Acinetobacter baumannii 625974
- **Pfam Domain**: PF00069
- **InterPro**: IPR000719, IPR011009
- **GO Terms**: F:ATP binding, F:protein serine/threonine kinase activity
- **Gene3D**: 1.10.510.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>A5UG81</u> | undetected | No | PF06293 | **IPR011009**, IPR022826 | C:plasma membrane, **F:ATP binding**, F:kinase activity, F:phosphotransferase activity, alcohol group as acceptor, P:lipopolysaccharide core region biosynthetic process | **1.10.510.10** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P44033</u> | undetected | No | PF07804 | IPR012893, IPR052028 | C:cytosol, **F:protein serine/threonine kinase activity** | 1.10.1070.20 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P14181</u> | undetected | No | PF01633 | **IPR011009**, IPR052077 | - | 3.30.200.20, 3.90.1200.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| Q8EKA0 | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| <u>B2K7I7</u> | undetected | No | PF12592, PF17868, PF20030, PF20265 | IPR003593, IPR022547, IPR023671, IPR027417, IPR041538, … | C:cytoplasm, **F:ATP binding**, F:ATP hydrolysis activity | 1.20.58.1510, 2.40.128.430, 3.40.50.300 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Yersiniaceae > Yersinia |
| Q12SQ2 | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| <u>A1SW96</u> | undetected | No | PF01266, PF05430 | IPR006076, IPR008471, IPR017610, IPR023032, IPR029063, … | C:cytoplasm, F:flavin adenine dinucleotide binding, F:oxidoreductase activity, acting on the CH-NH group of donors, F:tRNA (5-methylaminomethyl-2-thiouridylate)(34)-methyltransferase activity, P:methylation, … | 3.30.9.10, 3.40.50.150, 3.50.50.60 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Psychromonadaceae > Psychromonas |
| <u>B4F0D4</u> | undetected | No | PF05762 | IPR002035, IPR008912, IPR023481, IPR036465 | C:cytosol | 3.40.50.410 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Morganellaceae > Proteus |
| <u>A3DA85</u> | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| <u>Q4QLU9</u> | undetected | No | PF05958 | IPR010280, IPR011825, IPR029063, IPR030390, IPR030391 | F:4 iron, 4 sulfur cluster binding, F:iron ion binding, F:rRNA (uridine-C5-)-methyltransferase activity, P:rRNA base methylation | 2.40.50.1070, 3.40.50.150 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |


### Query: A0A002

**Query Information:**
- **Organism**: Streptomyces viridosporus
- **Pfam Domain**: PF00005, PF00664
- **InterPro**: IPR003439, IPR003593, IPR011527, IPR027417, IPR036640, IPR039421
- **GO Terms**: C:plasma membrane, F:ABC-type transporter activity, F:ATP binding, F:ATP hydrolysis activity
- **Gene3D**: 1.20.1560.10, 3.40.50.300
- **Lineage**: Bacteria > Bacillati > Actinomycetota > Actinomycetes > Kitasatosporales > Streptomycetaceae > Streptomyces

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>P9WQJ3</u> | 28% | Yes | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled transmembrane transporter activity, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > Mycobacteriales > Mycobacteriaceae > Mycobacterium > Mycobacterium tuberculosis complex |
| <u>Q13BH6</u> | 29% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, F:ABC-type beta-glucan transporter activity, F:ABC-type oligopeptide transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Alphaproteobacteria > Hyphomicrobiales > Nitrobacteraceae > Rhodopseudomonas |
| <u>Q03024</u> | 31% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, IPR010128, **IPR011527**, IPR017871, … | **C:plasma membrane**, C:type I protein secretion system complex, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Pseudomonadales > Pseudomonadaceae > Pseudomonas |
| <u>Q20Z38</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, F:ABC-type beta-glucan transporter activity, F:ABC-type oligopeptide transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Alphaproteobacteria > Hyphomicrobiales > Nitrobacteraceae > Rhodopseudomonas |
| <u>P23886</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR014223, IPR017871, … | C:ATP-binding cassette (ABC) transporter complex, C:ATP-binding cassette (ABC) transporter complex, integrated substrate binding, **C:plasma membrane**, F:ABC-type heme transporter activity, **F:ATP binding**, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Enterobacterales > Enterobacteriaceae > Escherichia |
| <u>Q8P8W4</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR011917, IPR017871, … | **C:plasma membrane**, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled lipid transmembrane transporter activity, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Lysobacterales > Lysobacteraceae > Xanthomonas |
| Q51719 | 31% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR005876, IPR015856, **IPR027417**, … | C:ATP-binding cassette (ABC) transporter complex, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled transmembrane transporter activity, P:cobalt ion transport | **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > Propionibacteriales > Propionibacteriaceae > Propionibacterium |
| Q82MV1 | 30% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR017871, **IPR027417**, IPR050166 | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > **Kitasatosporales** > **Streptomycetaceae** > **Streptomyces** |
| <u>Q28433</u> | 27% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR013305, IPR017871, … | C:MHC class I peptide loading complex, C:membrane, F:ABC-type peptide antigen transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity**, … | **1.20.1560.10**, **3.40.50.300** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Euarchontoglires > Primates > Haplorrhini > Catarrhini > Hominidae > Gorilla |
| <u>A0K739</u> | 33% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR017871, **IPR027417**, IPR050166 | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Betaproteobacteria > Burkholderiales > Burkholderiaceae > Burkholderia > Burkholderia cepacia complex |


### Query: A0A009HN45

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR027417, IPR038718, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:helicase activity, F:hydrolase activity
- **Gene3D**: 3.40.50.10810, 3.40.50.300
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>A6QKD8</u> | undetected | No | PF01043, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:protein-exporting ATPase activity, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Staphylococcaceae > Staphylococcus |
| **A7MSB2** | 36% | Yes | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| <u>Q3K063</u> | undetected | No | PF01043, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:protein-exporting ATPase activity, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| **Q9ZDW2** | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > Alphaproteobacteria > Rickettsiales > Rickettsiaceae > Rickettsieae > Rickettsia > typhus group |
| <u>Q1MQP3</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR004027, IPR011115, IPR011116, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > Thermodesulfobacteriota > Desulfovibrionia > Desulfovibrionales > Desulfovibrionaceae > Lawsonia |
| <u>Q7VJC6</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR004027, IPR011115, IPR011116, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > Campylobacterota > Epsilonproteobacteria > Campylobacterales > Helicobacteraceae > Helicobacter |
| <u>B0BT63</u> | 34% | Yes | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Actinobacillus |
| <u>Q92H92</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, IPR004027, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > Alphaproteobacteria > Rickettsiales > Rickettsiaceae > Rickettsieae > Rickettsia > spotted fever group |
| **P52126** | undetected | No | PF00270, **PF00271** | **IPR001650**, IPR011545, **IPR014001**, **IPR027417**, IPR050699 | **F:ATP binding**, **F:helicase activity**, **F:hydrolase activity**, F:nucleic acid binding, P:defense response to virus, … | **3.40.50.300** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| <u>Q0HMR2</u> | 30% | No | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |


### Query: A0A009HQC9

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271, PF12137, PF18337, PF18339
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR022737, IPR023949, IPR027417, IPR038718, IPR040765, IPR040766, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:DNA binding, F:helicase activity, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription
- **Gene3D**: 2.30.30.140, 2.30.30.930, 3.30.360.80, 3.40.50.10810, 3.40.50.300, 6.10.140.1500
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **Q0HR19** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **Q0HMR2** | 44% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **A0KGL5** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Aeromonadales > Aeromonadaceae > Aeromonas |
| **A1A7A6** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **A7ZW09** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **B0BT63** | 40% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Actinobacillus |
| **A7MSB2** | 44% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| <u>Q48LP5</u> | 44% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Pseudomonas |
| **B5FI41** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |
| **Q5PDF0** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |


### Query: A0A009IB02

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00198, PF00364, PF02817
- **InterPro**: IPR000089, IPR001078, IPR003016, IPR004167, IPR011053, IPR023213, IPR036625, IPR050743
- **GO Terms**: C:cytoplasm, F:dihydrolipoyllysine-residue acetyltransferase activity, F:lipoic acid binding, P:pyruvate decarboxylation to acetyl-CoA
- **Gene3D**: 2.40.50.100, 3.30.559.10, 4.10.320.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **P10802** | 46% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, IPR006256, … | **C:cytoplasm**, C:pyruvate dehydrogenase complex, **F:dihydrolipoyllysine-residue acetyltransferase activity**, **F:lipoic acid binding**, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Azotobacter |
| <u>P11961</u> | 38% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | **C:cytoplasm**, **F:dihydrolipoyllysine-residue acetyltransferase activity**, **F:lipoic acid binding** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Anoxybacillaceae > Geobacillus |
| <u>Q9SQI8</u> | 42% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | C:chloroplast, C:chloroplast envelope, C:chloroplast stroma, C:chloroplast thylakoid, C:cytosol, … | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | Eukaryota > Viridiplantae > Streptophyta > Embryophyta > Tracheophyta > Spermatophyta > Magnoliopsida > eudicotyledons > Gunneridae > Pentapetalae > rosids > malvids > Brassicales > Brassicaceae > Camelineae > Arabidopsis |
| <u>P49786</u> | undetected | No | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Bacillaceae > Bacillus |
| **P22439** | 26% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | C:mitochondrial matrix, C:mitochondrion, C:pyruvate dehydrogenase complex, F:acyltransferase activity, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Laurasiatheria > Artiodactyla > Ruminantia > Pecora > Bovidae > Bovinae > Bos |
| <u>P43874</u> | 41% | Yes | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P29337</u> | 41% | Yes | **PF00364** | **IPR000089**, IPR001882, **IPR011053**, IPR050709 | P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| <u>P02904</u> | 40% | Yes | **PF00364** | **IPR000089**, IPR001882, **IPR011053**, IPR050709 | F:methylmalonyl-CoA carboxytransferase activity | **2.40.50.100** | **Bacteria** > Bacillati > Actinomycetota > Actinomycetes > Propionibacteriales > Propionibacteriaceae > Propionibacterium |
| <u>Q06881</u> | 32% | Yes | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR053217 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Cyanobacteriota > Cyanophyceae > Nostocales > Nostocaceae > Nostoc |
| <u>P0ABE1</u> | 36% | No | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Shigella |


## IVF-PQ


### Query: A0A009PCK4

**Query Information:**
- **Organism**: Acinetobacter baumannii 625974
- **Pfam Domain**: PF00069
- **InterPro**: IPR000719, IPR011009
- **GO Terms**: F:ATP binding, F:protein serine/threonine kinase activity
- **Gene3D**: 1.10.510.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>P14181</u> | undetected | No | PF01633 | **IPR011009**, IPR052077 | - | 3.30.200.20, 3.90.1200.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>A5UG81</u> | undetected | No | PF06293 | **IPR011009**, IPR022826 | C:plasma membrane, **F:ATP binding**, F:kinase activity, F:phosphotransferase activity, alcohol group as acceptor, P:lipopolysaccharide core region biosynthetic process | **1.10.510.10** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P44033</u> | undetected | No | PF07804 | IPR012893, IPR052028 | C:cytosol, **F:protein serine/threonine kinase activity** | 1.10.1070.20 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>Q4QLU9</u> | undetected | No | PF05958 | IPR010280, IPR011825, IPR029063, IPR030390, IPR030391 | F:4 iron, 4 sulfur cluster binding, F:iron ion binding, F:rRNA (uridine-C5-)-methyltransferase activity, P:rRNA base methylation | 2.40.50.1070, 3.40.50.150 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| Q8E9R5 | undetected | No | PF03109 | IPR004147, IPR010232, **IPR011009**, IPR045308, IPR050154 | C:plasma membrane, **F:ATP binding**, F:protein kinase activity, P:regulation of ubiquinone biosynthetic process, P:ubiquinone biosynthetic process | - | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| Q87PM1 | undetected | No | PF03881 | **IPR011009**, IPR016477 | **F:ATP binding**, F:kinase activity | 3.30.200.20, 3.90.1200.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| <u>A3DA85</u> | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| P75612 | undetected | No | PF00005 | IPR003439, IPR003593, IPR017871, IPR017911, IPR027417 | **F:ATP binding**, F:ATP hydrolysis activity | 3.40.50.300 | **Bacteria** > Bacillati > Mycoplasmatota > Mycoplasmoidales > Mycoplasmoidaceae > Mycoplasmoides |
| Q9CPH1 | undetected | No | PF05958 | IPR010280, IPR011825, IPR029063, IPR030390, IPR030391 | F:4 iron, 4 sulfur cluster binding, F:iron ion binding, F:rRNA (uridine-C5-)-methyltransferase activity, P:rRNA base methylation | 2.40.50.1070, 3.40.50.150 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Pasteurella |
| Q0I208 | undetected | No | PF03109 | IPR004147, IPR010232, **IPR011009**, IPR045308, IPR050154 | C:plasma membrane, **F:ATP binding**, F:protein kinase activity, P:regulation of ubiquinone biosynthetic process, P:ubiquinone biosynthetic process | - | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Histophilus |


### Query: A0A002

**Query Information:**
- **Organism**: Streptomyces viridosporus
- **Pfam Domain**: PF00005, PF00664
- **InterPro**: IPR003439, IPR003593, IPR011527, IPR027417, IPR036640, IPR039421
- **GO Terms**: C:plasma membrane, F:ABC-type transporter activity, F:ATP binding, F:ATP hydrolysis activity
- **Gene3D**: 1.20.1560.10, 3.40.50.300
- **Lineage**: Bacteria > Bacillati > Actinomycetota > Actinomycetes > Kitasatosporales > Streptomycetaceae > Streptomyces

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>A0K739</u> | 33% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR017871, **IPR027417**, IPR050166 | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Betaproteobacteria > Burkholderiales > Burkholderiaceae > Burkholderia > Burkholderia cepacia complex |
| Q7VZE5 | 30% | No | **PF00005**, PF12857, PF17850 | **IPR003439**, **IPR003593**, IPR005666, IPR008995, IPR017871, … | C:ATP-binding cassette (ABC) transporter complex, F:ABC-type sulfate transporter activity, F:ABC-type thiosulfate transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Betaproteobacteria > Burkholderiales > Alcaligenaceae > Bordetella |
| Q7WGW1 | 29% | No | **PF00005**, PF12857, PF17850 | **IPR003439**, **IPR003593**, IPR005666, IPR008995, IPR017871, … | C:ATP-binding cassette (ABC) transporter complex, F:ABC-type sulfate transporter activity, F:ABC-type thiosulfate transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Betaproteobacteria > Burkholderiales > Alcaligenaceae > Bordetella |
| Q21BF6 | 30% | No | **PF00005**, PF03459 | **IPR003439**, **IPR003593**, IPR004606, IPR005116, IPR008995, … | **C:plasma membrane**, F:ABC-type molybdate transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | 2.40.50.100, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Alphaproteobacteria > Hyphomicrobiales > Nitrobacteraceae > Rhodopseudomonas |
| Q9RKQ4 | 31% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR017871, **IPR027417** | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > **Kitasatosporales** > **Streptomycetaceae** > **Streptomyces** > Streptomyces albidoflavus group |
| Q4ZZK0 | 28% | No | **PF00005**, PF09383 | **IPR003439**, **IPR003593**, IPR017871, IPR018449, **IPR027417**, … | **C:plasma membrane**, F:ABC-type D-methionine transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | 3.30.70.260, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Pseudomonadales > Pseudomonadaceae > Pseudomonas > Pseudomonas syringae |
| Q3Z3V4 | 26% | No | **PF00005**, PF08352 | **IPR003439**, **IPR003593**, IPR013563, IPR017871, **IPR027417**, … | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity**, P:peptide transport, P:transmembrane transport | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Enterobacterales > Enterobacteriaceae > Shigella |
| P75796 | 26% | No | **PF00005**, PF08352 | **IPR003439**, **IPR003593**, IPR013563, IPR017871, **IPR027417**, … | C:ATP-binding cassette (ABC) transporter complex, substrate-binding subunit-containing, C:membrane, **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity**, … | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Enterobacterales > Enterobacteriaceae > Escherichia |
| B4TGI0 | 31% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR017871, IPR023693, **IPR027417**, … | **C:plasma membrane**, F:ABC-type vitamin B12 transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Enterobacterales > Enterobacteriaceae > Salmonella |
| A7ZLX1 | 44% | No | **PF00005** | **IPR003439**, **IPR003593**, **IPR027417**, IPR050107 | **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Enterobacterales > Enterobacteriaceae > Escherichia |


### Query: A0A009HN45

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR027417, IPR038718, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:helicase activity, F:hydrolase activity
- **Gene3D**: 3.40.50.10810, 3.40.50.300
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **A7MSB2** | 36% | Yes | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| **Q9ZDW2** | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > Alphaproteobacteria > Rickettsiales > Rickettsiaceae > Rickettsieae > Rickettsia > typhus group |
| **P52126** | undetected | No | PF00270, **PF00271** | **IPR001650**, IPR011545, **IPR014001**, **IPR027417**, IPR050699 | **F:ATP binding**, **F:helicase activity**, **F:hydrolase activity**, F:nucleic acid binding, P:defense response to virus, … | **3.40.50.300** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| Q99ZA5 | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| Q1JBD1 | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| P0C9B2 | undetected | No | **PF00176**, **PF00271** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR027417**, **IPR038718** | C:virion component, **F:ATP binding**, F:RNA helicase activity, **F:hydrolase activity**, P:DNA repair, … | **3.40.50.10810**, **3.40.50.300** | Viruses > Varidnaviria > Bamfordvirae > Nucleocytoviricota > Pokkesviricetes > Asfuvirales > Asfarviridae > Asfivirus > African swine fever virus |
| C0MBD7 | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| A3CNJ9 | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| Q8CWX7 | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| Q65191 | undetected | No | PF04851 | IPR006935, **IPR014001**, **IPR027417**, IPR050742 | **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, F:RNA helicase activity | **3.40.50.300** | Viruses > Varidnaviria > Bamfordvirae > Nucleocytoviricota > Pokkesviricetes > Asfuvirales > Asfarviridae > Asfivirus > African swine fever virus |


### Query: A0A009HQC9

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271, PF12137, PF18337, PF18339
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR022737, IPR023949, IPR027417, IPR038718, IPR040765, IPR040766, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:DNA binding, F:helicase activity, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription
- **Gene3D**: 2.30.30.140, 2.30.30.930, 3.30.360.80, 3.40.50.10810, 3.40.50.300, 6.10.140.1500
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **Q0HR19** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **Q0HMR2** | 44% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **A0KGL5** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Aeromonadales > Aeromonadaceae > Aeromonas |
| **A1A7A6** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **A7ZW09** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **B0BT63** | 40% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Actinobacillus |
| **A7MSB2** | 44% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| **B5FI41** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |
| **Q5PDF0** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |
| Q3KGV8 | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Pseudomonas |


### Query: A0A009IB02

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00198, PF00364, PF02817
- **InterPro**: IPR000089, IPR001078, IPR003016, IPR004167, IPR011053, IPR023213, IPR036625, IPR050743
- **GO Terms**: C:cytoplasm, F:dihydrolipoyllysine-residue acetyltransferase activity, F:lipoic acid binding, P:pyruvate decarboxylation to acetyl-CoA
- **Gene3D**: 2.40.50.100, 3.30.559.10, 4.10.320.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **P10802** | 46% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, IPR006256, … | **C:cytoplasm**, C:pyruvate dehydrogenase complex, **F:dihydrolipoyllysine-residue acetyltransferase activity**, **F:lipoic acid binding**, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Azotobacter |
| <u>P11961</u> | 38% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | **C:cytoplasm**, **F:dihydrolipoyllysine-residue acetyltransferase activity**, **F:lipoic acid binding** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Anoxybacillaceae > Geobacillus |
| <u>P49786</u> | undetected | No | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Bacillaceae > Bacillus |
| **P22439** | 26% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | C:mitochondrial matrix, C:mitochondrion, C:pyruvate dehydrogenase complex, F:acyltransferase activity, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Laurasiatheria > Artiodactyla > Ruminantia > Pecora > Bovidae > Bovinae > Bos |
| <u>P43874</u> | 41% | Yes | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P29337</u> | 41% | Yes | **PF00364** | **IPR000089**, IPR001882, **IPR011053**, IPR050709 | P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| <u>P02904</u> | 40% | Yes | **PF00364** | **IPR000089**, IPR001882, **IPR011053**, IPR050709 | F:methylmalonyl-CoA carboxytransferase activity | **2.40.50.100** | **Bacteria** > Bacillati > Actinomycetota > Actinomycetes > Propionibacteriales > Propionibacteriaceae > Propionibacterium |
| <u>P0ABE1</u> | 36% | No | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Shigella |
| <u>Q06881</u> | 32% | Yes | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR053217 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Cyanobacteriota > Cyanophyceae > Nostocales > Nostocaceae > Nostoc |
| Q4R4J7 | undetected | No | PF00076 | IPR000504, IPR003954, IPR012677, IPR034230, IPR034233, … | **C:cytoplasm**, C:nucleolus, C:ribonucleoprotein complex, F:RNA binding, F:telomeric DNA binding | 3.30.70.330 | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Euarchontoglires > Primates > Haplorrhini > Catarrhini > Cercopithecidae > Cercopithecinae > Macaca |


## Neural LSH


### Query: A0A009PCK4

**Query Information:**
- **Organism**: Acinetobacter baumannii 625974
- **Pfam Domain**: PF00069
- **InterPro**: IPR000719, IPR011009
- **GO Terms**: F:ATP binding, F:protein serine/threonine kinase activity
- **Gene3D**: 1.10.510.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>A5UG81</u> | undetected | No | PF06293 | **IPR011009**, IPR022826 | C:plasma membrane, **F:ATP binding**, F:kinase activity, F:phosphotransferase activity, alcohol group as acceptor, P:lipopolysaccharide core region biosynthetic process | **1.10.510.10** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P44033</u> | undetected | No | PF07804 | IPR012893, IPR052028 | C:cytosol, **F:protein serine/threonine kinase activity** | 1.10.1070.20 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P14181</u> | undetected | No | PF01633 | **IPR011009**, IPR052077 | - | 3.30.200.20, 3.90.1200.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| Q8EKA0 | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| <u>B2K7I7</u> | undetected | No | PF12592, PF17868, PF20030, PF20265 | IPR003593, IPR022547, IPR023671, IPR027417, IPR041538, … | C:cytoplasm, **F:ATP binding**, F:ATP hydrolysis activity | 1.20.58.1510, 2.40.128.430, 3.40.50.300 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Yersiniaceae > Yersinia |
| Q12SQ2 | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| <u>A1SW96</u> | undetected | No | PF01266, PF05430 | IPR006076, IPR008471, IPR017610, IPR023032, IPR029063, … | C:cytoplasm, F:flavin adenine dinucleotide binding, F:oxidoreductase activity, acting on the CH-NH group of donors, F:tRNA (5-methylaminomethyl-2-thiouridylate)(34)-methyltransferase activity, P:methylation, … | 3.30.9.10, 3.40.50.150, 3.50.50.60 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Psychromonadaceae > Psychromonas |
| <u>B4F0D4</u> | undetected | No | PF05762 | IPR002035, IPR008912, IPR023481, IPR036465 | C:cytosol | 3.40.50.410 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Morganellaceae > Proteus |
| <u>A3DA85</u> | undetected | No | PF00581 | IPR001763, IPR017582, IPR036873 | F:tRNA 2-selenouridine synthase activity, F:transferase activity, transferring alkyl or aryl (other than methyl) groups, P:tRNA wobble uridine modification | 3.40.250.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| <u>Q4QLU9</u> | undetected | No | PF05958 | IPR010280, IPR011825, IPR029063, IPR030390, IPR030391 | F:4 iron, 4 sulfur cluster binding, F:iron ion binding, F:rRNA (uridine-C5-)-methyltransferase activity, P:rRNA base methylation | 2.40.50.1070, 3.40.50.150 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |


### Query: A0A002

**Query Information:**
- **Organism**: Streptomyces viridosporus
- **Pfam Domain**: PF00005, PF00664
- **InterPro**: IPR003439, IPR003593, IPR011527, IPR027417, IPR036640, IPR039421
- **GO Terms**: C:plasma membrane, F:ABC-type transporter activity, F:ATP binding, F:ATP hydrolysis activity
- **Gene3D**: 1.20.1560.10, 3.40.50.300
- **Lineage**: Bacteria > Bacillati > Actinomycetota > Actinomycetes > Kitasatosporales > Streptomycetaceae > Streptomyces

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>P9WQJ3</u> | 28% | Yes | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled transmembrane transporter activity, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > Mycobacteriales > Mycobacteriaceae > Mycobacterium > Mycobacterium tuberculosis complex |
| <u>Q13BH6</u> | 29% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, F:ABC-type beta-glucan transporter activity, F:ABC-type oligopeptide transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Alphaproteobacteria > Hyphomicrobiales > Nitrobacteraceae > Rhodopseudomonas |
| <u>Q03024</u> | 31% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, IPR010128, **IPR011527**, IPR017871, … | **C:plasma membrane**, C:type I protein secretion system complex, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Pseudomonadales > Pseudomonadaceae > Pseudomonas |
| <u>Q20Z38</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR017871, **IPR027417**, … | **C:plasma membrane**, F:ABC-type beta-glucan transporter activity, F:ABC-type oligopeptide transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity** | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Alphaproteobacteria > Hyphomicrobiales > Nitrobacteraceae > Rhodopseudomonas |
| <u>P23886</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR014223, IPR017871, … | C:ATP-binding cassette (ABC) transporter complex, C:ATP-binding cassette (ABC) transporter complex, integrated substrate binding, **C:plasma membrane**, F:ABC-type heme transporter activity, **F:ATP binding**, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Enterobacterales > Enterobacteriaceae > Escherichia |
| <u>Q8P8W4</u> | 28% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR011917, IPR017871, … | **C:plasma membrane**, **F:ABC-type transporter activity**, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled lipid transmembrane transporter activity, … | **1.20.1560.10**, **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Lysobacterales > Lysobacteraceae > Xanthomonas |
| Q51719 | 31% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR005876, IPR015856, **IPR027417**, … | C:ATP-binding cassette (ABC) transporter complex, **F:ATP binding**, **F:ATP hydrolysis activity**, F:ATPase-coupled transmembrane transporter activity, P:cobalt ion transport | **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > Propionibacteriales > Propionibacteriaceae > Propionibacterium |
| Q82MV1 | 30% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR017871, **IPR027417**, IPR050166 | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > **Bacillati** > **Actinomycetota** > **Actinomycetes** > **Kitasatosporales** > **Streptomycetaceae** > **Streptomyces** |
| <u>Q28433</u> | 27% | No | **PF00005**, **PF00664** | **IPR003439**, **IPR003593**, **IPR011527**, IPR013305, IPR017871, … | C:MHC class I peptide loading complex, C:membrane, F:ABC-type peptide antigen transporter activity, **F:ATP binding**, **F:ATP hydrolysis activity**, … | **1.20.1560.10**, **3.40.50.300** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Euarchontoglires > Primates > Haplorrhini > Catarrhini > Hominidae > Gorilla |
| <u>A0K739</u> | 33% | No | **PF00005** | **IPR003439**, **IPR003593**, IPR017871, **IPR027417**, IPR050166 | **C:plasma membrane**, **F:ATP binding**, **F:ATP hydrolysis activity** | **3.40.50.300** | **Bacteria** > Pseudomonadati > Pseudomonadota > Betaproteobacteria > Burkholderiales > Burkholderiaceae > Burkholderia > Burkholderia cepacia complex |


### Query: A0A009HN45

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR027417, IPR038718, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:helicase activity, F:hydrolase activity
- **Gene3D**: 3.40.50.10810, 3.40.50.300
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| <u>A6QKD8</u> | undetected | No | PF01043, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:protein-exporting ATPase activity, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Staphylococcaceae > Staphylococcus |
| **A7MSB2** | 36% | Yes | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| <u>Q3K063</u> | undetected | No | PF01043, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:protein-exporting ATPase activity, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| **Q9ZDW2** | undetected | No | **PF00271**, PF02151, PF04851, PF12344, PF17757 | **IPR001650**, IPR001943, IPR004807, IPR006935, **IPR014001**, … | C:cytoplasm, C:excinuclease repair complex, **F:ATP binding**, F:ATP hydrolysis activity, F:DNA binding, … | **3.40.50.300**, 4.10.860.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > Alphaproteobacteria > Rickettsiales > Rickettsiaceae > Rickettsieae > Rickettsia > typhus group |
| <u>Q1MQP3</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR004027, IPR011115, IPR011116, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > Thermodesulfobacteriota > Desulfovibrionia > Desulfovibrionales > Desulfovibrionaceae > Lawsonia |
| <u>Q7VJC6</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, **IPR001650**, IPR004027, IPR011115, IPR011116, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > Campylobacterota > Epsilonproteobacteria > Campylobacterales > Helicobacteraceae > Helicobacter |
| <u>B0BT63</u> | 34% | Yes | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Actinobacillus |
| <u>Q92H92</u> | undetected | No | PF01043, PF02810, PF07516, PF07517, PF21090 | IPR000185, IPR004027, IPR011115, IPR011116, IPR011130, … | C:cell envelope Sec protein transport complex, C:cytosol, C:plasma membrane, **F:ATP binding**, F:metal ion binding, … | 1.10.3060.10, **3.40.50.300**, 3.90.1440.10 | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > Alphaproteobacteria > Rickettsiales > Rickettsiaceae > Rickettsieae > Rickettsia > spotted fever group |
| **P52126** | undetected | No | PF00270, **PF00271** | **IPR001650**, IPR011545, **IPR014001**, **IPR027417**, IPR050699 | **F:ATP binding**, **F:helicase activity**, **F:hydrolase activity**, F:nucleic acid binding, P:defense response to virus, … | **3.40.50.300** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| <u>Q0HMR2</u> | 30% | No | **PF00176**, **PF00271**, PF12137, PF18337, PF18339 | **IPR000330**, **IPR001650**, **IPR014001**, IPR022737, IPR023949, … | **F:ATP binding**, F:DNA binding, **F:helicase activity**, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription | 2.30.30.140, 2.30.30.930, 3.30.360.80, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |


### Query: A0A009HQC9

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00176, PF00271, PF12137, PF18337, PF18339
- **InterPro**: IPR000330, IPR001650, IPR014001, IPR022737, IPR023949, IPR027417, IPR038718, IPR040765, IPR040766, IPR049730, IPR057342
- **GO Terms**: F:ATP binding, F:DNA binding, F:helicase activity, F:hydrolase activity, acting on acid anhydrides, P:regulation of DNA-templated transcription
- **Gene3D**: 2.30.30.140, 2.30.30.930, 3.30.360.80, 3.40.50.10810, 3.40.50.300, 6.10.140.1500
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **Q0HR19** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **Q0HMR2** | 44% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Alteromonadales > Shewanellaceae > Shewanella |
| **A0KGL5** | 45% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Aeromonadales > Aeromonadaceae > Aeromonas |
| **A1A7A6** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **A7ZW09** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Escherichia |
| **B0BT63** | 40% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Actinobacillus |
| **A7MSB2** | 44% | No | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Vibrionales > Vibrionaceae > Vibrio |
| <u>Q48LP5</u> | 44% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Pseudomonas |
| **B5FI41** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |
| **Q5PDF0** | 42% | Yes | **PF00176**, **PF00271**, **PF12137**, **PF18337**, **PF18339** | **IPR000330**, **IPR001650**, **IPR014001**, **IPR022737**, **IPR023949**, … | **F:ATP binding**, **F:DNA binding**, **F:helicase activity**, **F:hydrolase activity, acting on acid anhydrides**, **P:regulation of DNA-templated transcription** | **2.30.30.140**, **2.30.30.930**, **3.30.360.80**, **3.40.50.10810**, **3.40.50.300**, … | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Salmonella |


### Query: A0A009IB02

**Query Information:**
- **Organism**: Acinetobacter baumannii (strain 1295743)
- **Pfam Domain**: PF00198, PF00364, PF02817
- **InterPro**: IPR000089, IPR001078, IPR003016, IPR004167, IPR011053, IPR023213, IPR036625, IPR050743
- **GO Terms**: C:cytoplasm, F:dihydrolipoyllysine-residue acetyltransferase activity, F:lipoic acid binding, P:pyruvate decarboxylation to acetyl-CoA
- **Gene3D**: 2.40.50.100, 3.30.559.10, 4.10.320.10
- **Lineage**: Bacteria > Pseudomonadati > Pseudomonadota > Gammaproteobacteria > Moraxellales > Moraxellaceae > Acinetobacter > Acinetobacter calcoaceticus/baumannii complex

**Neighbor Annotations:**

| Neighbor | Blast ID | In BLAST? | Pfam | InterPro | GO | Gene3D | Lineage |
|---|---|---|---|---|---|---|---|
| **P10802** | 46% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, IPR006256, … | **C:cytoplasm**, C:pyruvate dehydrogenase complex, **F:dihydrolipoyllysine-residue acetyltransferase activity**, **F:lipoic acid binding**, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pseudomonadales > Pseudomonadaceae > Azotobacter |
| <u>P11961</u> | 38% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | **C:cytoplasm**, **F:dihydrolipoyllysine-residue acetyltransferase activity**, **F:lipoic acid binding** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Anoxybacillaceae > Geobacillus |
| <u>Q9SQI8</u> | 42% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | C:chloroplast, C:chloroplast envelope, C:chloroplast stroma, C:chloroplast thylakoid, C:cytosol, … | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | Eukaryota > Viridiplantae > Streptophyta > Embryophyta > Tracheophyta > Spermatophyta > Magnoliopsida > eudicotyledons > Gunneridae > Pentapetalae > rosids > malvids > Brassicales > Brassicaceae > Camelineae > Arabidopsis |
| <u>P49786</u> | undetected | No | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Bacillota > Bacilli > Bacillales > Bacillaceae > Bacillus |
| **P22439** | 26% | Yes | **PF00198**, **PF00364**, **PF02817** | **IPR000089**, **IPR001078**, **IPR003016**, **IPR004167**, **IPR011053**, … | C:mitochondrial matrix, C:mitochondrion, C:pyruvate dehydrogenase complex, F:acyltransferase activity, **P:pyruvate decarboxylation to acetyl-CoA** | **2.40.50.100**, **3.30.559.10**, **4.10.320.10** | Eukaryota > Metazoa > Chordata > Craniata > Vertebrata > Euteleostomi > Mammalia > Eutheria > Laurasiatheria > Artiodactyla > Ruminantia > Pecora > Bovidae > Bovinae > Bos |
| <u>P43874</u> | 41% | Yes | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Pasteurellales > Pasteurellaceae > Haemophilus |
| <u>P29337</u> | 41% | Yes | **PF00364** | **IPR000089**, IPR001882, **IPR011053**, IPR050709 | P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Bacillota > Bacilli > Lactobacillales > Streptococcaceae > Streptococcus |
| <u>P02904</u> | 40% | Yes | **PF00364** | **IPR000089**, IPR001882, **IPR011053**, IPR050709 | F:methylmalonyl-CoA carboxytransferase activity | **2.40.50.100** | **Bacteria** > Bacillati > Actinomycetota > Actinomycetes > Propionibacteriales > Propionibacteriaceae > Propionibacterium |
| <u>Q06881</u> | 32% | Yes | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR053217 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > Bacillati > Cyanobacteriota > Cyanophyceae > Nostocales > Nostocaceae > Nostoc |
| <u>P0ABE1</u> | 36% | No | **PF00364** | **IPR000089**, IPR001249, IPR001882, **IPR011053**, IPR050709 | C:acetyl-CoA carboxylase complex, F:acetyl-CoA carboxylase activity, P:fatty acid biosynthetic process | **2.40.50.100** | **Bacteria** > **Pseudomonadati** > **Pseudomonadota** > **Gammaproteobacteria** > Enterobacterales > Enterobacteriaceae > Shigella |
