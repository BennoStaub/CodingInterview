class Node():
	def __init__(self, value, children=None):
		self.value = value
		self.visited = False
		self.children = []
		if children:
			self.children = children

	def addChild(self, child):
		self.children.append(child)

	def addChildren(self, children):
		for child in children:
			self.addChild(child)

	def removeChild(self, node):
		self.children.remove(node)


class Graph():

	def __init__(self):
		self.nodes = []

	def addNode(self, node):
		self.nodes.append(node)

	def removeNode(self, node):
		self.nodes.remove(node)

	def initiateGraph(self):
		# Initiate graph from page 107
		node0 = Node(0)
		node1 = Node(1)
		node2 = Node(2)
		node3 = Node(3)
		node4 = Node(4)
		node5 = Node(5)
		node0.addChildren([node1, node4, node5])
		node1.addChildren([node3, node4])
		node2.addChildren([node1])
		node3.addChildren([node2, node4])
		self.addNode(node0)
		self.addNode(node1)
		self.addNode(node2)
		self.addNode(node3)
		self.addNode(node4)
		self.addNode(node5)

	def printGraph(self):
		for node in self.nodes:
			children = []
			for child in node.children:
				children.append(child.value)
			print('node ' + str(node.value) + ' with children ' + str(children))