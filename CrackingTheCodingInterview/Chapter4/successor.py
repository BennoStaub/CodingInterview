import sys
sys.path.append('../../DataStructures/')
from graph import BinaryTreeNode, initiateBinarySearchTree, printBinaryTree

def successor(start, node):
	if node is not start:
		return node
	elif node.right:
		temp = node.right
		while temp.left:
			temp = temp.left
		return temp
	else:
		return successor(start, node.parent)

if __name__ == '__main__':
	tree = initiateBinarySearchTree([1,3,4,6,9,12,15,19,22,25])
	printBinaryTree(tree)
	print(successor(tree.right, tree.right).value)