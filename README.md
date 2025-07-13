# Microbial Network Resilience

This repository contains the complete set of data, analysis scripts, and visualization results for the study:

**_“Emergence of Collective Intelligence Through the Disruption of Microbial Behavior: Does Homeostatic Breakdown Catalyze Creative Problem Solving?”_**

---

## Overview

This study explores how gut microbial dysbiosis—particularly under chronic stress—may not merely signal dysfunction but instead catalyze adaptive reorganization in host-microbiota systems. Using microbial co-occurrence network analysis and computational perturbation modeling, we identify hub taxa, assess modularity, and analyze the emergence of novel communication pathways that may underlie resilience and collective behavior.

---

## Repository Structure

The repository is organized as follows:

<code> stress_microbiome_networks/
├── README.md ← Project description and usage
├── scripts/ ← Python and QIIME2 analysis scripts
│ ├── network_analysis.py
│ └── alpha_beta_diversity.qzv
├── data/ ← Preprocessed input data
│ ├── group_Control_for_sparcc.tsv
│ ├── stress_oll2809_cytoscape_edges.tsv
│ └── taxonomy.tsv
└── results/
├── Cytoscape_networks/ ← Cytoscape .cys files or network exports
└── figures/ ← Network and diversity visualization outputs
</code>



---

## Data Availability

All raw 16S rRNA sequencing data used in this study were obtained from the NCBI Sequence Read Archive (SRA) under BioProject [**PRJNA956987**](https://www.ncbi.nlm.nih.gov/bioproject/956987).

Sample accessions:  
**SRR28210342** through **SRR28210381**  
These samples represent fecal microbiota from a mouse model of depression, including:

- **Control**
- **Stress + Vehicle**
- **Stress + _Lactobacillus paragasseri_ OLL2809**

---

## Contact

For questions, contributions, or suggestions, please contact:  
**hyechin kong** – [hyechin.kong@kcl.ak.uk]  
Or open an issue on this repository.

---

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.


All raw sequencing data used in this study were obtained from the NCBI Sequence Read Archive (SRA) under BioProject [PRJNA956987](https://www.ncbi.nlm.nih.gov/bioproject/956987). Sample accessions include SRR28210342 through SRR28210381. These samples represent fecal microbiota from a mouse model of depression, including control, vehicle-treated, and Lactobacillus OLL2809 intervention groups.

