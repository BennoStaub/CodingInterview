import sys
sys.path.append('../../DataStructures/')
from graph import Node, Graph, initiateGraph, initiateBinarySearchTree

def validateBST(graph):
	BST = True
	for node in graph.nodes:
		if len(node.children) == 2:
			if not node.children[0].value <= node.value < node.children[1].value:
				BST = False
		elif len(node.children) == 1:
			if not node.children[0].value <= node.value:
				BST = False
	return BST


if __name__ == '__main__':
	graph = Graph()
	initiateBinarySearchTree(graph, [1,3,4,6,9,12,15,19,22,25])
	graph.printGraph()
	print([node.value for node in graph.nodes])
	print(validateBST(graph))