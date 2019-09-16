def flipBitToWin(value):
	max_sum = 0
	previous_sum = 0
	current_sum = 0
	previous_bit = 0
	for bit in value:
		if bit == '1':
			current_sum += 1
		else:
			candidate = max(current_sum + previous_sum + 1, current_sum + 1)
			max_sum = max(max_sum, candidate)
			previous_sum = current_sum
			current_sum = 0
	candidate = max(current_sum + previous_sum + 1, current_sum + 1)
	max_sum = max(max_sum, candidate)

if __name__ == '__main__':
	value = '11011101111'
	flipBitToWin(value)