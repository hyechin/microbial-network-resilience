Microbial Network Resilience
This repository contains the complete set of data, analysis scripts, and visualization results for the study:

“Emergence of Collective Intelligence Through the Disruption of Microbial Behavior: Does Homeostatic Breakdown Catalyze Creative Problem Solving?”

---

## Directory Structure

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


All raw sequencing data used in this study were obtained from the NCBI Sequence Read Archive (SRA) under BioProject [PRJNA956987](https://www.ncbi.nlm.nih.gov/bioproject/956987). Sample accessions include SRR28210342 through SRR28210381. These samples represent fecal microbiota from a mouse model of depression, including control, vehicle-treated, and Lactobacillus OLL2809 intervention groups.

