import sys
sys.path.append('../../DataStructures/')
from graph import BinaryTreeNode, initiateBinaryTree, printBinaryTree

def checkMatch(root1, root2):
	if root1 and root2:
		if root1.value == root2.value:
			check = checkMatch(root1.left, root2.left)
			if check:
				check = checkMatch(root1.right, root2.right)
			return check 
		else:
			return False
	elif not root1 and not root2:
		return True
	else:
		return False

def checkSubtree(root1, root2):
	if root1:
		if root1.value == root2.value:
			return checkMatch(root1, root2)
		else:
			check = checkSubtree(root1.left, root2)
			if check:
				return True
			check = checkSubtree(root1.right, root2)
			return check
	return False


if __name__ == '__main__':
	root1 = initiateBinaryTree()
	root2 = initiateBinaryTree()
	root2 = root2.left
	#root2.right = BinaryTreeNode(10)
	print('root1')
	printBinaryTree(root1)
	print('root2')
	printBinaryTree(root2)
	print(checkSubtree(root1, root2))