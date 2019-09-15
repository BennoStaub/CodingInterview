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

class BinaryTreeNode():
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def addLeft(self, child):
		self.left = child


	def addRight(self, child):
		self.right = child

	def removeLeft(self):
		self.left = None

	def removeRight(self):
		self.right = None


def initiateBinaryTree():
	# Initiate binary tree:
	#			10
	#		  /    \
	#		 5		7
	#	   /  \      \
	#	  12  15	  9
	#	 /  \		
	#	4	 8
	root = BinaryTreeNode(10)
	root = root
	root.left = BinaryTreeNode(5, parent=root)
	root.right = BinaryTreeNode(7, parent=root)
	root.left.left = BinaryTreeNode(12, parent=root.left)
	root.left.left.left = BinaryTreeNode(4, parent=root.left.left)
	root.left.left.right = BinaryTreeNode(8, parent=root.left.left)
	root.left.right = BinaryTreeNode(15, parent=root.left)
	root.right.right = BinaryTreeNode(9, parent=root.right)
	return root

def printBinaryTree(tree):
	level = [tree]
	children = []
	while level:
		printList = [node.value for node in level]
		print(printList)
		for node in level:
			if node.left:
				children.append(node.left)
			if node.right:
				children.append(node.right)
		level = children
		children = []

def initiateBinarySearchTree(values=[1,3,4,6,9,12,15,19,22,25], parent=None):
	if values:
		node = BinaryTreeNode(values[len(values) // 2], parent=parent)
		if values[:len(values) // 2]:
			node.left = initiateBinarySearchTree(values[:len(values) // 2], node)
		if values[len(values) // 2 + 1:]:
			node.right = initiateBinarySearchTree(values[len(values) // 2 + 1:], node)
		return node





class Graph():

	def __init__(self):
		self.nodes = []

	def addNode(self, node):
		self.nodes.append(node)

	def addNodes(self, nodes):
		for node in nodes:
			self.addNode(node)

	def removeNode(self, node):
		self.nodes.remove(node)

	def addEdge(self, s, t):
		s.children.append(t)

	def printGraph(self):
		for node in self.nodes:
			children = []
			for child in node.children:
				children.append(child.value)
			print('node ' + str(node.value) + ' with children ' + str(children))

def initiateGraph():
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
	graph = Graph()
	graph.addNodes([node0, node1, node2, node3, node4, node5])
	return graph

def initiateBinarySearchTreeGraph(graph, values):
	if values:
		node = Node(values[len(values) // 2])
		graph.addNode(node)
		if values[:len(values) // 2]:
			node.children.append(initiateBinarySearchTreeGraph(graph, values[:len(values) // 2]))
		if values[len(values) // 2 + 1:]:
			node.children.append(initiateBinarySearchTreeGraph(graph, values[len(values) // 2 + 1:]))
		return node


