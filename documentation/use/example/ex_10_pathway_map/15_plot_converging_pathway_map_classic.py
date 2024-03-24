"""
Pathway map for converging pathways
===================================
"""

from io import StringIO

import matplotlib.pyplot as plt

from adaptation_pathways.graph import action_level_by_first_occurrence, conversion
from adaptation_pathways.io import text
from adaptation_pathways.plot import init_axes
from adaptation_pathways.plot import plot_classic_pathway_map as plot


actions, colour_by_action = text.read_actions(
    StringIO(
        """
current #ff4c566a
a #ffbf616a
b #ffd08770
c #ffebcb8b
d #ffa3be8c
"""
    )
)
sequences, tipping_point_by_action = text.read_sequences(
    StringIO(
        """
current current 2030
current a 2040
current b 2050
current c 2060
a d[1] 2070
b d[2] 2070
c d[3] 2070
"""
    )
)
sequence_graph = conversion.sequences_to_sequence_graph(sequences)
pathway_map = conversion.sequence_graph_to_pathway_map(sequence_graph)

level_by_action = action_level_by_first_occurrence(sequences)
colour_by_action_name = {
    action.name: colour for action, colour in colour_by_action.items()
}

pathway_map.assign_tipping_points(tipping_point_by_action)
pathway_map.set_attribute("level_by_action", level_by_action)
pathway_map.set_attribute("colour_by_action_name", colour_by_action_name)

_, axes = plt.subplots(layout="constrained")
init_axes(axes)
plot(axes, pathway_map)
plt.show()
