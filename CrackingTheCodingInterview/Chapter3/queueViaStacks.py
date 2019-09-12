class MyQueue():

	def __init__(self):
		self.stack = []
		self.queue = []

	def push(self, value):
		return self.stack.append(value)

	def pop(self):
		while self.stack:
			self.queue.append(self.stack.pop())
		pop_element = self.queue.pop()
		while self.queue:
			self.stack.append(self.queue.pop())
		return pop_element


if __name__ == '__main__':
	queue = MyQueue()
	queue.push(1)
	queue.push(2)
	queue.push(3)
	queue.push(4)
	queue.push(5)
	print(queue.stack)
	print(queue.pop())
	print(queue.stack)