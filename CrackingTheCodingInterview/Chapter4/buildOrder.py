import sys
sys.path.append('../../DataStructures/')
from graph import Node, Graph

def buildOrder(reversed_graph):
	order = []
	nodes = reversed_graph.nodes
	while nodes:
		for node in nodes:
			if len(node.children) == 0:
				order.append(node)
				nodes.remove(node)
				for rest_node in nodes:
					if node in rest_node.children:
						rest_node.children.remove(node)
	print([node.value for node in order])


if __name__ == '__main__':
	reversed_graph = Graph()
	a = Node('a')
	b = Node('b')
	c = Node('c')
	d = Node('d')
	e = Node('e')
	f = Node('f')
	reversed_graph.addNodes([a,b,c,d,e,f])
	reversed_graph.addEdge(d,a)
	reversed_graph.addEdge(b,f)
	reversed_graph.addEdge(d,b)
	reversed_graph.addEdge(a,f)
	reversed_graph.addEdge(c,d)
	reversed_graph.printGraph()
	buildOrder(reversed_graph)