import sys
sys.path.append('../../DataStructures/')
from graph import BinaryTreeNode, initiateBinarySearchTree, printBinaryTree
from random import randint

class BinarySearchTree():

	def __init__(self, root):
		self.root = root

	def addNode(self, node):
		temp = self.root
		while temp:
			if node.value <= temp.value:
				if temp.left:
					temp = temp.left
				else:
					temp.left = node
					node.parent = temp
					print(temp.value)
					print('left')
					print(temp.left.value)
					break
			else:
				if temp.right:
					temp = temp.right
				else:
					temp.right = node
					node.parent = temp
					print(temp.value)
					print('right')
					print(temp.right.value)
					break
		self.nodes.append(node)

	def deleteNode(self, value):
		node = self.findNode(value)
		self.nodes.remove(node)
		if node.right and node.left:
			min_right_subtree = self.findMin(node.right)
			if node.parent.left is node:
				self.deleteNode(min_right_subtree.value)
				node.parent.left = min_right_subtree
				min_right_subtree.left = node.left
				min_right_subtree.right = node.right
			else:
				self.deleteNode(min_right_subtree.value)
				node.parent.right = min_right_subtree
				min_right_subtree.left = node.left
				min_right_subtree.right = node.right
		elif node.right:
			if node.parent.left is node:
				node.parent.left = node.right
			else:
				node.parent.right = node.right
		elif node.left:
			if node.parent.left is node:
				node.parent.left = node.left
			else:
				node.parent.right = node.left
		else:
			if node.parent.left is node:
				node.parent.left = None
			else:
				node.parent.right = None

	def findMin(self, root):
		temp = root
		while temp.left:
			temp = temp.left
		return temp

	def findNode(self, value):
		temp = self.root
		while temp and temp.value is not value:
			if value <= temp.value:
				temp = temp.left
			else:
				temp = temp.right
		if temp:
			return temp
		else:
			print('node not found')
			return -1

	def getRandomNode(self):
		node_list = self.getNodeList(self.root)
		index = randint(0,len(node_list)-1)
		return node_list[index]

	def getNodeList(self, root):
		if root:
			if root.left:
				list_left = self.getNodeList(root.left)
			else:
				list_left = []
			if root.right:
				list_right = self.getNodeList(root.right)
			else:
				list_right = []
			return [root] + list_left + list_right
		else:
			return [root]






if __name__ == '__main__':
	root = initiateBinarySearchTree()
	bst = BinarySearchTree(root)
	bst.getRandomNode()
	printBinaryTree(bst.root)


