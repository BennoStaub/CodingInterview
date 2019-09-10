import sys
sys.path.append('../../DataStructures/')
from linkedList import Node, initiateLinkedList, printLinkedList


def removeDups(head):
	pointer1 = head
	pointer2 = head
	while pointer1 != None:
		while pointer2 != None and pointer2.next != None:
			if pointer2.next.value == pointer1.value:
				pointer2.next = pointer2.next.next
			pointer2 = pointer2.next
		pointer1 = pointer1.next
		if pointer1 != None:
			pointer2 = pointer1.next
	return head


if __name__ == '__main__':
	head = initiateLinkedList()
	printLinkedList(head)
	removeDups(head)
	print('removed')
	printLinkedList(head)
