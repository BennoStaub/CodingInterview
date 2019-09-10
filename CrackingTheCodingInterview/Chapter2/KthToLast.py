import sys
sys.path.append('../../DataStructures/')
from linkedList import Node, initiateLinkedList, printLinkedList, computeLength

def KthToLast(head, k):
	length = computeLength(head)
	if length < k:
		return -1
	kth = head
	runner = head
	for _ in range(k-1):
		runner = runner.next
	while runner.next:
		kth = kth.next
		runner = runner.next
	return kth


if __name__ == '__main__':
	head = initiateLinkedList([10,4,7,3,8,4,3,56,8,5,2,4,6,8,4,3])
	kth = KthToLast(head,5)
	printLinkedList(kth)
