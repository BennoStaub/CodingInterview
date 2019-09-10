class Node():
	def __init__(self,value):
		self.value = value
		self.next = None

def initiateLinkedList():
	head = Node(5)
	values = [10,4,7,3,8,4,3,56,8,5,2,4,6,8,4,3]
	temp = head
	for value in values:
		node = Node(value)
		temp.next = node
		temp = node
	return head

def printLinkedList(head):
	temp = head
	while temp != None:
		print(temp.value)
		temp = temp.next
	return head