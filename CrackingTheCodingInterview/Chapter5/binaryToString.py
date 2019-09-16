def binaryToString(x):
	string = ''
	exponent = -1
	while x and len(string) <= 31:
		subtrahend = 2 ** exponent
		print('next')
		print(x)
		print(subtrahend)
		if x >= subtrahend:
			string += '1'
			x -= subtrahend
		else:
			string += '0'
		print(string)
		exponent -= 1
	if len(string) <= 31:
		return '.' + string
	else:
		return 'ERROR'


if __name__ == '__main__':
	x = 0.72
	print(binaryToString(x))