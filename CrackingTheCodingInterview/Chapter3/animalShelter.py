class AnimalShelterNode():
	def __init__(self, animal, name):
		self.animal = animal
		self.name = name
		self.next = None


class AnimalShelter(AnimalShelterNode):

	def __init__(self, animal, name):
		self.head = AnimalShelterNode(animal, name)

	def push(self, node):
		runner = self.head
		while runner.next:
			runner = runner.next
		runner.next = node

	def dequeueAny(self):
		node = self.head
		self.head = self.head.next
		return node

	def dequeueDog(self):
		if self.head.animal == 'dog':
			return self.dequeueAny()
		runner = self.head
		while runner.next and runner.next.animal != 'dog':
			runner = runner.next
		if runner.next:
			node = runner.next
			runner.next = node.next
			return node
		else:
			return -1

	def dequeueCat(self):
		if self.head.animal == 'cat':
			return self.dequeueAny()
		runner = self.head
		while runner.next and runner.next.animal != 'cat':
			runner = runner.next
		if runner.next:
			node = runner.next
			runner.next = node.next
			return node
		else:
			return -1



	def print(self):
		runner = self.head
		while runner:
			print(runner.animal + ' called ' + runner.name)
			runner = runner.next


if __name__ == '__main__':
	shelter = AnimalShelter('cat', 'Ninja')
	shelter.push(AnimalShelterNode('cat', 'Ninja'))
	shelter.push(AnimalShelterNode('dog', 'Ninja'))
	shelter.push(AnimalShelterNode('dog','Ali'))
	shelter.push(AnimalShelterNode('cat','Lara'))
	shelter.push(AnimalShelterNode('dog','Leila'))
	shelter.print()
	print('dequeueAny')
	shelter.dequeueAny()
	shelter.print()
	print('dequeueDog')
	shelter.dequeueDog()
	shelter.print()
	print('dequeueCat twice')
	shelter.dequeueCat()
	shelter.dequeueCat()
	shelter.print()