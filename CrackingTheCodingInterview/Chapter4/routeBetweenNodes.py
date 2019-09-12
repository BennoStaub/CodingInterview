import sys
sys.path.append('../../DataStructures/')
from graph import Node, Graph, initiateGraph

def breadthFirstSeach(graph, s, t):
	if s is t:
		return -1

	queue = []
	s.visited = True
	for child in s.children:
		if not child.visited:
			queue.append(child)
	while queue:
		node = queue.pop(0)
		node.visited = True
		if node is t:
			return True
		for child in node.children:
			if not child.visited:
				queue.append(child)
	return False


if __name__ == '__main__':
	graph = initiateGraph()
	graph.printGraph()
	print(breadthFirstSeach(graph, graph.nodes[0], graph.nodes[1]))


