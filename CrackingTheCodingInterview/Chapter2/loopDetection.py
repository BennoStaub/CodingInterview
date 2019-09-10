import sys
sys.path.append('../../DataStructures/')
from linkedList import Node, initiateLinkedList, printLinkedList


def loop_detection(head):
    fast = slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break
    if fast is None or fast.next is None:
        return None
    slow = head
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    return fast


if __name__ == '__main__':
	head = initiateLinkedList([10,4,7,3,8,4,3,56,8,5,2,4,6,8,4,3])
	temp = head
	for _ in range(10):
		temp = temp.next
	print(temp.value)
	last = head
	while last.next is not None:
		last = last.next
	last.next = temp
	print(loop_detection(head).value)