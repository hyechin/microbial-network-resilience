# Microbial Network Resilience

This repository contains all data, scripts, and visualization results for the study:

**"Emergence of Collective Intelligence Through the Disruption of Microbial Behavior: Does Homeostatic Breakdown Catalyze Creative Problem Solving?"**

## Overview

This study investigates how gut microbial dysbiosis, especially under chronic stress, can lead to adaptive network reorganization rather than solely pathological collapse. Through microbial co-occurrence network analysis and computational perturbation modeling, we identify hub taxa, analyze modularity, and assess the emergence of novel communication routes in microbiome structure.

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
