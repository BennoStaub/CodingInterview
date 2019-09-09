def palindromePermutation(string):
	string = string.lower()
	string = string.replace(' ', '')
	bit_vector = [0 for _ in range(26)]
	for char in string:
		index = ord(char) - ord('a')
		bit_vector[index] += 1
	number_odd = 0
	for bit in bit_vector:
		if (bit % 2 == 1):
			number_odd += 1
	return number_odd <= 1


if __name__ == '__main__':
	string = 'Tact Coa'
	print(palindromePermutation(string))