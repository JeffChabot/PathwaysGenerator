import enum
import typing

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from .colour import (
    default_edge_colours,
    default_font_colour,
    default_node_colours_pathway_graph,
    default_node_colours_pathway_map,
    default_node_colours_sequence_graph,
)
from .layout.pathway_graph import default_layout as pathway_graph_layout
from .layout.pathway_map import classic_layout as classic_pathway_map_layout
from .layout.pathway_map import default_layout as default_pathway_map_layout
from .layout.sequence_graph import default_layout as sequence_graph_layout
from .pathway_graph import PathwayGraph
from .pathway_map import PathwayMap
from .sequence_graph import SequenceGraph


PathwayMapLayout = enum.Enum("PathwayMapLayout", ["DEFAULT", "CLASSIC"])


def init_plot(
    title: str,
    graph: nx.DiGraph,
    layout: dict[typing.Any, np.ndarray],
    colours: list[tuple[float, float, float, float]] | None = None,
    edge_colours: list[tuple[float, float, float, float]] | None = None,
) -> None:
    plt.rc(
        "axes.spines", **{"bottom": False, "left": False, "right": False, "top": False}
    )
    # plt.clf()

    # draw_options = {
    #     "with_labels": True,
    #     "font_size": "small",
    #     "font_weight": "bold",
    # }

    _, axis = plt.subplots()

    axis.set_title(title)
    # nx.draw_networkx(
    #     graph, pos=layout, node_color=colours, edge_color=edge_colours, **draw_options
    # )
    nx.draw_networkx_edges(
        graph,
        pos=layout,
        edge_color=edge_colours,
        width=1.0,
        arrows=False,
    )
    nx.draw_networkx_nodes(
        graph,
        pos=layout,
        node_color=colours,
        node_size=100,
        linewidths=0.25,
        edgecolors=default_font_colour(),
    )
    nx.draw_networkx_labels(
        graph,
        pos=layout,
        font_size="x-small",
        font_weight="bold",
        verticalalignment="bottom",
        horizontalalignment="right",
        font_color=default_font_colour(),
    )


def save_plot(pathname: str) -> None:
    plt_options = {
        "bbox_inches": "tight",
        "transparent": True,
    }
    plt.savefig(pathname, **plt_options)


def plot_sequence_graph(
    sequence_graph: SequenceGraph,
    colours: list[tuple[float, float, float, float]] | None = None,
    edge_colours: list[tuple[float, float, float, float]] | None = None,
) -> None:
    if colours is None:
        colours = default_node_colours_sequence_graph(sequence_graph)

    if edge_colours is None:
        edge_colours = default_edge_colours(sequence_graph)

    init_plot(
        "Sequence graph",
        sequence_graph.graph,
        sequence_graph_layout(sequence_graph),
        colours,
        edge_colours,
    )


def plot_and_save_sequence_graph(
    sequence_graph: SequenceGraph,
    pathname: str,
    colours: list[tuple[float, float, float, float]] | None = None,
    edge_colours: list[tuple[float, float, float, float]] | None = None,
) -> None:
    plot_sequence_graph(sequence_graph, colours, edge_colours)
    save_plot(pathname)


def plot_pathway_graph(
    pathway_graph: PathwayGraph,
    colours: list[tuple[float, float, float, float]] | None = None,
    edge_colours: list[tuple[float, float, float, float]] | None = None,
) -> None:
    if colours is None:
        colours = default_node_colours_pathway_graph(pathway_graph)

    if edge_colours is None:
        edge_colours = default_edge_colours(pathway_graph)

    init_plot(
        "Pathway graph",
        pathway_graph.graph,
        pathway_graph_layout(pathway_graph),
        colours,
        edge_colours,
    )


def plot_and_save_pathway_graph(
    pathway_graph: PathwayGraph,
    pathname: str,
    colours: list[tuple[float, float, float, float]] | None = None,
    edge_colours: list[tuple[float, float, float, float]] | None = None,
) -> None:
    plot_pathway_graph(pathway_graph, colours, edge_colours)
    save_plot(pathname)


def plot_pathway_map(
    pathway_map: PathwayMap,
    layout: PathwayMapLayout = PathwayMapLayout.DEFAULT,
    colours: list[tuple[float, float, float, float]] | None = None,
    edge_colours: list[tuple[float, float, float, float]] | None = None,
) -> None:
    if layout == PathwayMapLayout.CLASSIC:
        pathway_map_layout = classic_pathway_map_layout
    else:
        pathway_map_layout = default_pathway_map_layout

    if colours is None:
        colours = default_node_colours_pathway_map(pathway_map)

    if edge_colours is None:
        edge_colours = default_edge_colours(pathway_map)

    init_plot(
        "Pathway map",
        pathway_map.graph,
        pathway_map_layout(pathway_map),
        colours,
        edge_colours,
    )


def plot_and_save_pathway_map(
    pathway_map: PathwayMap,
    pathname: str,
    layout: PathwayMapLayout = PathwayMapLayout.DEFAULT,
    colours: list[tuple[float, float, float, float]] | None = None,
    edge_colours: list[tuple[float, float, float, float]] | None = None,
) -> None:
    plot_pathway_map(pathway_map, layout, colours, edge_colours)
    save_plot(pathname)
