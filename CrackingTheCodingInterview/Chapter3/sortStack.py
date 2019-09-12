class SortStack():

		def __init__(self):
			self.sort_stack = []
			self.helper_stack = []

		def push(self, value):
			if self.sort_stack:
				while self.sort_stack and value > self.sort_stack[-1]:
					self.helper_stack.append(self.sort_stack.pop())
				self.sort_stack.append(value)
				while self.helper_stack:
					self.sort_stack.append(self.helper_stack.pop())
			else:
				return self.sort_stack.append(value)

		def pop(self):
			return self.sort_stack.pop()


if __name__ == '__main__':
	stack = SortStack()
	stack.push(10)
	stack.push(5)
	stack.push(7)
	stack.push(13)
	stack.push(9)
	stack.push(4)
	stack.push(4)
	stack.push(20)
	print(stack.sort_stack)