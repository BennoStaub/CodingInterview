def stringRotation(string1, string2):
	if len(string1) == len(string2):
		string1 += string1
		return isSubstring(string1, string2)
	else:
		return False

def isSubstring(string1, string2):
	return string2 in string1

if __name__ == '__main__':
	string1 = 'watterbottle'
	string2 = 'erbottlewatt'
	print(stringRotation(string1, string2))

