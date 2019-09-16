def conversion(a, b):
	number_different_bits = 0
	while a or b:
		if a & 1 != b & 1:
			number_different_bits += 1
		a >>= 1
		b >>= 1
	return number_different_bits


if __name__ == '__main__':
	a = 29
	b = 15
	print(conversion(a,b))

