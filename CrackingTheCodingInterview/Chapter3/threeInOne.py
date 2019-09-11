class ThreeInOne():

	def __init__(self, size):
		self.size = size
		self.stackArray = [None] * self.size
		self.ends = [0,1,2]


	def push(self, stack_number, value):
		for index in range(self.size-2, self.ends[stack_number], -1):
			self.stackArray[index + 1] = self.stackArray[index]
		self.stackArray[self.ends[stack_number]] = value
		for index in range(stack_number, 3):
			self.ends[index] += 1

	def pop(self, stack_number):
		value = self.stackArray[self.ends[stack_number]-1]
		print('value ' + str(value))
		for index in range(self.ends[stack_number] - 1, self.size - 2):
			self.stackArray[index] = self.stackArray[index + 1]
			print('printing Array')
			self.printArray()
		for index in range(stack_number, 3):
			self.ends[index] -= 1
		return value

	def printArray(self):
		for element in self.stackArray:
			print(element)


if __name__ == '__main__':
	stack = ThreeInOne(15)
	stack.push(0,14)
	stack.push(0,4)
	stack.push(0,7)
	stack.push(1,8)
	stack.push(2,10)
	stack.pop(0)
	stack.pop(0)
	stack.printArray()
	print(stack.ends)