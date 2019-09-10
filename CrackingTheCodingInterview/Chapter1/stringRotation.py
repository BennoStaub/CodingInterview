def stringRotation(string1, string2):
	i = 0
	length = len(string1)
	found = False
	for index in range(len(string2)):
		if string2[index] == string1[0] and string2[index:] == string1[:length-index-1]:
			found = True
			break;
	if found:
		return isSubstring(string1, string2[:index])
	else:
		return False

def isSubstring(string1, string2):
	return string2 in string1

if __name__ == '__main__':
	string1 = 'watterbottle'
	string2 = 'erbottlewat'
	print(stringRotation(string1, string2))

