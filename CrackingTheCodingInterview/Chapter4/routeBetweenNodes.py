import sys
sys.path.append('../../DataStructures/')
from graph import Node, Graph

def breadthFirstSeach(graph, s, t):
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
	graph = Graph()
	graph.initiateGraph()
	print(graph.nodes)
	graph.printGraph()
	print(breadthFirstSeach(graph, graph.nodes[3], graph.nodes[0]))


