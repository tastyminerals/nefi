#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
(from nefi1)
Implementation of an algorithm which filters a graph for connected components
and keeps only the largest of them, e.g remove all connected components except
the 4 largest.
"""
import cv2
import networkx as nx
from _alg import *


__author__ = {"Pavel Shkadzko": "p.shkadzko@gmail.com"}


class AlgBody(Algorithm):
    """
    Keep only largest connected component algorithm implementation.
    """
    def __init__(self):
        """
        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriate category

        """
        Algorithm.__init__(self)
        self.name = "Keep only largest connected component"
        self.parent = "Graph Filtering"

    def process(self, graph):
        """
        Keep only largest connected component from nefi1.

        Args:
            | *graph* : an undirected networkx Graph

        Raises:
            | *ValueError* : means filtering failed due to the number
              of components not to be removed is negative.

        Returns:
            | *graph* : a filtered networkx Graph

        """
        try:
            connected = sorted(list(nx.connected_component_subgraphs(graph)),
                               key=lambda x: x.number_of_nodes(),
                               reverse=True)
            to_be_removed = connected[self.largest_components_to_keep:]
            for subgraph in to_be_removed:
                graph.remove_nodes_from(subgraph)
        except ValueError as e:
            print('ValueError exception:', e)
        self.result['graph'] = graph


if __name__ == '__main__':
    pass
