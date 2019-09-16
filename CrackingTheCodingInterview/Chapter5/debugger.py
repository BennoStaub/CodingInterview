from random import randint

def debugger(n):
	return ((n & n-1) == 0)


if __name__ == '__main__':
	for i in range(257):
		if debugger(i):
			print(i)
		print(debugger(i))