class Node():
	def __init__(self,value):
		self.value = value
		self.next = None

def initiateLinkedList(values):
	head = Node(values[0])
	temp = head
	for value in values[1:]:
		node = Node(value)
		temp.next = node
		temp = node
	return head

def printLinkedList(head):
	temp = head
	while temp:
		print(temp.value)
		temp = temp.next
	return head

def computeLength(head):
	if head == None:
		return 0
	else:
		length = 0
		while head:
			length += 1
			head = head.next
		return length