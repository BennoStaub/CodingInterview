def zeroMatrix(matrix):
	zero_indices = []
	columns = len(matrix)
	rows = len(matrix[0])
	for i in range(columns):
		for j in range(rows):
			if matrix[i][j] == 0:
				zero_indices.append((i,j))
	for i,j in zero_indices:
		for row in range(rows):
			matrix[i][row] = 0
		for column in range(columns):
			matrix[column][j] = 0
	return matrix


if __name__ == '__main__':
	matrix = [[1,2,3,0,5,3,0],[4,7,2,6,4,6,3],[1,1,1,1,1,0,1],[2,2,2,2,2,2,2]]
	print(zeroMatrix(matrix))