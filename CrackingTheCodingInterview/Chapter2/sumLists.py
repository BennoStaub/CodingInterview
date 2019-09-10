import sys
sys.path.append('../../DataStructures/')
from linkedList import Node, initiateLinkedList, printLinkedList, computeLength

def sumLists(head1, head2):
	add_next = 0
	value = head1.value + head2.value
	if value >= 10:
		value -= 10
		add_next = 1
	sumlist = Node(value)
	s = sumlist
	head1 = head1.next
	head2 = head2.next
	while head1 and head2:
		value = head1.value + head2.value + add_next
		add_next = 0
		if value >= 10:
			value -= 10
			add_next = 1
		s.next = Node(value)
		s = s.next
		head1 = head1.next
		head2 = head2.next
	while head1:
		s.next = head1
		if add_next:
			if s.next.value + 1 < 10:
				s.next.value += 1
				add_next = 0
			else:
				s.next.value -= 9
				add_next = 1
		head1 = head1.next
		s = s.next
	while head2:
		s.next = head2
		if add_next:
			if s.next.value + 1 < 10:
				s.next.value += 1
				add_next = 0
			else:
				s.next.value -= 9
				add_next = 1
		head2 = head2.next
		s = s.next
	if add_next:
		s.next = Node(1)
	printLinkedList(sumlist)




if __name__ == '__main__':
	head1 = initiateLinkedList([7,1,9])
	head2 = initiateLinkedList([5,9,2,9])
	printLinkedList(head1)
	print('second')
	printLinkedList(head2)
	sumLists(head1, head2)
