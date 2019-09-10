import sys
sys.path.append('../../DataStructures/')
from linkedList import Node, initiateLinkedList, printLinkedList, computeLength
from KthToLast import KthToLast

def palindrome(head):
	length = computeLength(head)
	for index in range(length // 2):
		temp = head
		for _ in range(index-1):
			temp = temp.next
		kth = KthToLast(head, index)
		if temp.value != kth.value:
			return False
	return True



if __name__ == '__main__':
	head = initiateLinkedList(['t','a','c','o','o','c','a','t'])
	printLinkedList(head)
	print(palindrome(head))