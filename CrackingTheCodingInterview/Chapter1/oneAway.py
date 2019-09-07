def oneAway(base_string, check_string):
	if len(base_string) == len(check_string):
		return check_replace(base_string, check_string)
	elif len(base_string) < len(check_string):
		return check_insert(base_string, check_string)
	else:
		return check_insert(check_string, base_string)
	


def check_replace(base_string, check_string):
	edited = False
	for base_char, check_char in zip(base_string, check_string):
		if base_char != check_char:
			if edited:
				return False
			edited = True
	return True

def check_insert(small_string, big_string):
	i, j = 0,0
	edited = False
	while i < len(small_string) and j < len(big_string):
		print small_string[i]
		print big_string[j]
		print 'next'
		if small_string[i] != big_string[j]:
			if edited:
				return False
			edited = True
			j += 1
		else:
			i += 1
			j += 1
	return True


if __name__ == '__main__':
	base_string = 'pale'
	check_string = 'ple'
	print oneAway(base_string, check_string)