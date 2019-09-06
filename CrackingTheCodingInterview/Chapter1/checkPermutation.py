def checkPermutation(base_string, check_string):
	bit_vector = [0 for _ in xrange(26)]
	for char in base_string:
		index = ord(char) - ord('a')
		bit_vector[index] += 1
	for char in check_string:
		index = ord(char) - ord('a')
		bit_vector[index] -= 1
	for bit in bit_vector:
		if bit != 0:
			return False
	return True



if __name__ == '__main__':
	base_string = 'abbcccdddd'
	check_string = 'abcdbcdcdd'
	print checkPermutation(base_string, check_string)
