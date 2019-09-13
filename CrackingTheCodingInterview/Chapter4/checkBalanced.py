import sys
sys.path.append('../../DataStructures/')
from graph import BinaryTreeNode, initiateBinaryTree


def checkBalanced(root):
	left = getDepth(tree.left, 0)
	right = getDepth(tree.right, 0)
	return abs(left - right) <= 1

def getDepth(root, depth):
	if root:
		depth_left = getDepth(root.left, depth + 1)
		depth_right = getDepth(root.right, depth + 1)
	else:
		depth_left = depth_right = depth
	if depth_left > depth_right:
		return depth_left
	else:
		return depth_right

if __name__ == '__main__':
	tree = initiateBinaryTree()
	tree.left.left.left.left = BinaryTreeNode(20)
	print(checkBalanced(tree))
