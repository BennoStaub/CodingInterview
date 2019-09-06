def URLify(string):
	return string.replace(' ', '%20')


if __name__ == '__main__':
	string = 'Mr John Smith'
	print URLify(string)