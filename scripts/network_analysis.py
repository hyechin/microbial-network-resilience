
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load SparCC correlation matrix
cor_matrix = pd.read_csv('data/group_Control_for_sparcc.tsv', sep='\t', index_col=0)

# Threshold correlation values
threshold = 0.3
edges = []
for i in cor_matrix.index:
    for j in cor_matrix.columns:
        val = cor_matrix.loc[i, j]
        if abs(val) >= threshold and i != j:
            edges.append((i, j, val))

# Create graph
G = nx.Graph()
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Basic network statistics
degrees = dict(G.degree())
nx.set_node_attributes(G, degrees, 'degree')

# Draw graph
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw_networkx_nodes(G, pos, node_size=[v*10 for v in degrees.values()], node_color='green', alpha=0.6)
nx.draw_networkx_edges(G, pos, alpha=0.3)
nx.draw_networkx_labels(G, pos, font_size=6)
plt.title('Microbial Co-occurrence Network (|r| > 0.3)')
plt.axis('off')
plt.tight_layout()
plt.savefig('results/figures/control_network_graph.png', dpi=300)
plt.show()

