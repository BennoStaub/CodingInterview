def stringCompression(string):
	new_string = ''
	take_new = False
	count_vector = [0 for _ in range(26)]
	for char in string:
		index = ord(char) - ord('a')
		count_vector[index] += 1
	for index in range(len(count_vector)):
		if count_vector[index] > 0:
			new_string = new_string + chr(index + ord('a')) + str(count_vector[index])
	if len(new_string) < len(string):
		return new_string
	else:
		return string


if __name__ == '__main__':
	string = 'abcdefghijksasfasfafafsfaergsggsdsafasfsmnopqrstuvwxyzf'
	print(stringCompression(string))