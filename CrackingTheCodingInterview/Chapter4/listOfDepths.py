import sys
sys.path.append('../../DataStructures/')
from graph import Node, Graph, initiateBinarySearchTreeGraph
from linkedList import Node as LinkedListNode, printLinkedList


def listOfDepths(graph):
	visiting = [graph.nodes[0]]
	children = []
	listOfDepths = []
	depth = 0
	while visiting:
		for node in visiting:
			for child in node.children:
				children.append(child)
			if not len(listOfDepths) > depth:
				listOfDepths.append(LinkedListNode(node.value))
			else:
				temp = listOfDepths[depth]
				while temp.next:
					temp = temp.next
				temp.next = LinkedListNode(node.value)
		depth += 1
		visiting = children
		children = []
	for head in listOfDepths:
		print('next level')
		printLinkedList(head)


if __name__ == '__main__':
	graph = Graph()
	initiateBinarySearchTreeGraph(graph, [1,3,4,6,9,12,15,19,22,25])
	listOfDepths(graph)
