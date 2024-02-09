"""
Pathway map for converging pathways
===================================
"""

from io import StringIO

import matplotlib.pyplot as plt

from adaptation_pathways.graph import read_sequences, sequence_graph_to_pathway_map
from adaptation_pathways.plot.pathway_map.default import plot


sequence_graph, _ = read_sequences(
    StringIO(
        """
current a
current b
current c
a d
b d
c d
"""
    )
)
pathway_map = sequence_graph_to_pathway_map(sequence_graph)

plot(pathway_map)
plt.show()
