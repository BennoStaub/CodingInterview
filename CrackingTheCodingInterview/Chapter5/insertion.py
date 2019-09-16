def insertion(N,M,i,j):
	mask = getMask(i, j)
	N_cleared = clearbits(N,mask)
	return insertbits(N,M,i)

def getMask(i, j):
	mask = 1 << (j -i)
	mask <<= i
	return mask

def clearbits(N,mask):
	return N & ~mask

def insertbits(N,M,i):
	return N | (M << i)


if __name__ == '__main__':
	N = 1024
	M = 19
	i = 2
	j = 6
	print(insertion(N,M,i,j))