import sys
sys.path.append('../../DataStructures/')
from graph import Node, Graph, initiateGraph, initiateBinarySearchTree

graph = Graph()
initiateBinarySearchTree(graph, [1,3,4,6,9,12,15,19,22,25,30,38])
graph.printGraph()
