import sys
sys.path.append('../../DataStructures/')
from linkedList import Node, initiateLinkedList, printLinkedList, computeLength

def deleteMiddleNode(middleNode):
	middleNode.value = middleNode.next.value
	middleNode.next = middleNode.next.next


if __name__ == '__main__':
	head = initiateLinkedList()
	printLinkedList(head)
	middleNode = head
	for _ in range(5):
		middleNode = middleNode.next
	print('middleNode')
	print(middleNode.value)
	deleteMiddleNode(middleNode)
	print('deleted')
	printLinkedList(head)

