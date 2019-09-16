import sys
sys.path.append('../../DataStructures/')
from graph import BinaryTreeNode, initiateBinaryTree


def getPaths(root):
	if root:
		if root.left:
			left_path = [[root.value]] + getPaths(root.left)
		else:
			left_path = []
		if root.right:
			right_path = [[root.value]] + getPaths(root.right)
		else:
			right_path = []
		print('next')
		print(root.value)
		print(left_path)
		print(right_path)
		return [root.value] + left_path + right_path

	else:
		return []


if __name__ == '__main__':
	root = initiateBinaryTree()
	paths = getPaths(root)
	print(paths)