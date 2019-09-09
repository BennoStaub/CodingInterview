import math

def rotateMatrix(matrix):
	N = len(matrix)
	for layer in range(N // 2):
		first, last = layer, N-1-layer
		for i in range(first, last):
			top = matrix[layer][i]
			matrix[layer][i] = matrix[N-1-i][layer]
			matrix[N-1-i][layer] = matrix[N-1-layer][N-1-i]
			matrix[N-1-layer][N-1-i] = matrix[i][N-1-layer]
			matrix[i][N-1-layer] = top
			print(matrix)
	print(matrix)


if __name__ == '__main__':
	matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
	rotateMatrix(matrix)