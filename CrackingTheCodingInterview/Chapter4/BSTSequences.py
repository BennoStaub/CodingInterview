import sys
sys.path.append('../../DataStructures/')
from graph import BinaryTreeNode, initiateBinarySearchTree, printBinaryTree


def BSTSequences(root):
	if root:
		left_sequences = BSTSequences(root.left)
		right_sequences = BSTSequences(root.right)
		seq = []
		if left_sequences:
			for left_sequence in left_sequences:
				if right_sequences:
					for right_sequence in right_sequences:
						sequence = [root.value] + left_sequence + right_sequence
						seq.append(sequence)
						sequence = [root.value] + right_sequence + left_sequence
						seq.append(sequence)
				else:
					sequence = [root.value] + left_sequence
					seq.append(sequence)
		else:
			if right_sequences:
				for right_sequence in right_sequences:
					sequence = [root.value] + right_sequence
					seq.append(sequence)
			else:
				seq.append([root.value])
		print(seq)
		return seq
	else:
		return []


if __name__ == '__main__':
	root = initiateBinarySearchTree([1,3,4,6,9, 12, 15, 19, 22, 25])
	BSTSequences(root)