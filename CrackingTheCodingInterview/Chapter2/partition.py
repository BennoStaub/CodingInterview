import sys
sys.path.append('../../DataStructures/')
from linkedList import Node, initiateLinkedList, printLinkedList, computeLength

def partition(head, x):
	if head.value >= x:
		smaller_x = None
		bigger_x = Node(head.value)
	else:
		smaller_x = Node(head.value)
		bigger_x = None
	runner = head.next
	s = smaller_x
	b = bigger_x
	while runner:
		if runner.value >= x:
			if b:
				b.next = Node(runner.value)
				b = b.next
			else:
				b = Node(runner.value)
				b.next = None
				bigger_x = b
		else:
			if s:
				s.next = Node(runner.value)
				s = s.next
			else:
				s = Node(runner.value)
				s.next = None
				smaller_x = s
		runner = runner.next
	s.next = bigger_x
	print('done')
	printLinkedList(smaller_x)


if __name__ == '__main__':
	head = initiateLinkedList()
	printLinkedList(head)
	partition(head, 6)
