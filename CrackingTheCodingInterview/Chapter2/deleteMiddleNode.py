import sys
sys.path.append('../../DataStructures/')
from linkedList import Node, initiateLinkedList, printLinkedList, computeLength

def deleteMiddleNode(middleNode):
	middleNode.value = middleNode.next.value
	middleNode.next = middleNode.next.next


if __name__ == '__main__':
	head = initiateLinkedList([10,4,7,3,8,4,3,56,8,5,2,4,6,8,4,3])
	printLinkedList(head)
	middleNode = head
	for _ in range(5):
		middleNode = middleNode.next
	print('middleNode')
	print(middleNode.value)
	deleteMiddleNode(middleNode)
	print('deleted')
	printLinkedList(head)

