def pairwiseSwap(value):
	even_mask = 1
	while even_mask <= value:
		even_mask <<= 2
		even_mask += 1
	odd_mask = 2
	while odd_mask <= value:
		odd_mask <<= 2
		odd_mask += 2
	even = even_mask & value
	odd = odd_mask & value
	even <<= 1
	odd >>= 1
	return even | odd


if __name__ == '__main__':
	value = 3678 # swapped result is 3501
	print(pairwiseSwap(value))
