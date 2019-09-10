import sys
sys.path.append('../../DataStructures/')
from linkedList import Node, initiateLinkedList, printLinkedList, computeLength

def intersection(head1, head2):
	if haveIntersection(head1, head2):
		length1 = computeLength(head1)
		length2 = computeLength(head2)
		if length1 >= length2:
			for _ in range(length1 - length2):
				head1 = head1.next
		else:
			for _ in range(length2 - length1):
				head2 = head2.next
		while head1 != head2:
			head1 = head1.next
			head2 = head2.next
		return head1
	else:
		return -1

def haveIntersection(head1, head2):
	last1 = head1
	last2 = head2
	while last1.next:
		last1 = last1.next
	while last2.next:
		last2 = last2.next
	return last1 == last2


if __name__ == '__main__':
	head1 = initiateLinkedList([10,4,7,3,8,4,3,56,8,5,2,4,6,8,4,3])
	head2 = initiateLinkedList([3,11,5,7,8,5,3,2,4,5,7,8,5,])
	temp1 = head1
	temp2 = head2
	for _ in range(7):
		temp1 = temp1.next
	for _ in range(4):
		temp2 = temp2.next
	temp1.next = temp2.next
	print('first')
	printLinkedList(head1)
	print('second')
	printLinkedList(head2)
	print('same')
	printLinkedList(intersection(head1, head2))
