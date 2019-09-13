import sys
sys.path.append('../../DataStructures/')
from graph import BinaryTreeNode, initiateBinaryTree


def firstCommonAncestor(s, t, ancestor):
	print('checking node ' + str(s.value) + ' against ' + str(t.value) + ' with ancestor ' + str(ancestor.value))
	if s is t:
		print('found')
		print('ancestor ' + str(ancestor.value))
		return ancestor
	if s.left:
		ancestor = firstCommonAncestor(s.left, t, ancestor)
	elif s.right:
		ancestor = firstCommonAncestor(s.right, t, ancestor)
	else:
		if s is s.parent.left:
			s.parent.left = None
		else:
			s.parent.right = None
		ancestor = firstCommonAncestor(s.parent, t, s.parent)
	return ancestor


if __name__ == '__main__':
	tree = initiateBinaryTree()
	found = firstCommonAncestor(tree.left.left.right, tree.right.right, tree.left.left.right)
	print(found.value)