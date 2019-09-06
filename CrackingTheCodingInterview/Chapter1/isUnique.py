def isUnique(string):
	char_bit_vector = [False for _ in range(26)]
	for  char in string:
		index = ord(char) - ord('a')
		if char_bit_vector[index]:
			return False
		char_bit_vector[index] = True;
	return True

if __name__ == '__main__':
	string = 'sdeyrkjly'
	print isUnique(string)
