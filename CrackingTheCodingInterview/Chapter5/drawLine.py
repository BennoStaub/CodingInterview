# Idea is correct, but python uses 32-bit signed integers
# Therefore it is technically not correct as we treat them
# here as unsigned 8-bit integers
def drawLine(screen, width, x1, x2, y):
	byte = left_border = y * width
	while byte <= y * (width + 1):
		if x1 <= 7 + 8*(byte-left_border) and x2 >= 7+ 8*(byte-left_border):
			num_bits = min(7 + 8*(byte-left_border) - x1 + 1, x2 - x1 + 1)
			mask = 1 << num_bits
			mask -= 1
			screen[byte] = mask
			x1 += num_bits
		else:
			# Even worse here using a sequence of 1s results in negative
			# value because the sign bit is a 1 too.
			num_bits = min(7 + 8*(byte-left_border) - x1 + 1, x2 - x1 + 1)
			mask = -1
			mask <<=  8 - num_bits
			screen[byte] = mask
			x1 += 8
		byte += 1
	print(screen)



if __name__ == '__main__':
	screen = [0,0,0,0,0,0,0,0,0,0,0,0] # len = 12
	width = 4
	x1 = 6
	x2 = 21
	y = 2
	drawLine(screen, width, x1, x2, y)