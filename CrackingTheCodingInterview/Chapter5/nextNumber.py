# Following the notation in the book solution:
# p is the position of the right-most non-trailing zero
# c0 is the number of zeros on the right of p
# c1 is the number of ones on the right of p


def nextNumber(value):
	c0, c1 = nextGetc0Andc1(value)
	flip_mask = 1 << (c0 + c1)
	flipped = value | flip_mask
	cleared = flipped & ~((1 << c0 + c1) - 1)
	return cleared | ((1 << (c1 - 1)) - 1)

def nextGetc0Andc1(value):
	c0 = 0
	c1 = 0
	while (value & 1) == 0 and value != 0:
		c0 += 1
		value >>= 1
	while value & 1 and value != 0:
		c1 += 1
		value >>= 1
	return c0, c1

def previousNumber(value):
	c0, c1 = prevGetc0Andc1(value)
	flip_mask = 1 << c0 + c1
	flipped = value & ~flip_mask
	cleared = flipped & ~((1 << c0 + c1) - 1)
	return cleared | 1 << c0 + c1 - 1

def prevGetc0Andc1(value):
	c0 = 0
	c1 = 0
	while value & 1 and value != 0:
		c1 += 1
		value >>= 1
	while (value & 1) == 0 and value != 0:
		c0 += 1
		value >>= 1
	return c0, c1




if __name__ == '__main__':
	value = 376
	print(nextNumber(value))
	print(previousNumber(value))
