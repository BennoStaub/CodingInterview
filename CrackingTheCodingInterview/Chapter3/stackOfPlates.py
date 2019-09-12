class SetOfStacks():
	def __init__(self, capacity):
		self.capacity = capacity
		self.set_of_stacks = [[]]
		self.number_stacks = 1

	def push(self, value):
		if len(self.set_of_stacks[self.number_stacks - 1]) < self.capacity:
			return self.set_of_stacks[self.number_stacks - 1].append(value)
		else:
			self.number_stacks += 1
			return self.set_of_stacks.append([value])

	def pop(self):
		if len(self.set_of_stacks[self.number_stacks - 1]) > 1:
			return self.set_of_stacks[self.number_stacks - 1].pop()
		else:
			self.number_stacks -= 1
			return self.set_of_stacks.pop()


if __name__ == '__main__':
	stacks = SetOfStacks(5)
	stacks.push(3)
	stacks.push(8)
	stacks.push(6)
	stacks.push(10)
	stacks.push(7)
	print(stacks.set_of_stacks)
	stacks.push(4)
	stacks.push(14)
	print(stacks.set_of_stacks)
	stacks.pop()
	print(stacks.set_of_stacks)
	stacks.pop()
	print(stacks.set_of_stacks)
	stacks.push(22)
	print(stacks.set_of_stacks)
	stacks.pop()
	stacks.pop()
	stacks.pop()
	print(stacks.set_of_stacks)