class StackMin():

	def __init__(self, element):
		self.stackMin = []
		self.minIndex = 0
		self.stackMin.append(element)

	def push(self, element):
		self.stackMin.append(element)
		if element < self.stackMin[self.minIndex]:
			self.minIndex = len(self.stackMin) - 1
		return self.stackMin

	def pop(self):
		return self.stackMin.pop()

	def min(self):
		return self.stackMin.pop(self.minIndex)

	def printStack(self):
		for element in self.stackMin:
			print(element)

if __name__ == '__main__':
	stack = StackMin(10)
	stack.push(5)
	stack.push(8)
	stack.push(13)
	stack.push(4)
	stack.push(11)
	stack.printStack()
	stack.min()
	print('min')
	stack.printStack()
	stack.pop()
	print('pop')
	stack.printStack()