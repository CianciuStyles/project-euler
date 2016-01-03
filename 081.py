import time

def main():
	# Read input from the file
	input_file = open("081.txt", "r")
	matrix = []
	for line in input_file.readlines():
		matrix_line = []
		for value in line.split(","):
			matrix_line.append(int(value))
		matrix.append(matrix_line)
	# print matrix

	# Navigate the matrix to find the minimal sum path
	row, col = 1, 1
	while col != 80:
		fillDiagonal(matrix, 0, col)
		col += 1
	while row != 80:
		fillDiagonal(matrix, row, col-1)
		row += 1

	print(matrix[79][79])

def fillDiagonal(matrix, row, col):
	while row != 80 and col != -1:
		# print "row: " + str(row) + " col: " + str(col)
		if row == 0:
			# print "row is 0"
			matrix[row][col] += matrix[row][col-1]
		elif col == 0:
			# print "col is 0"
			matrix[row][col] += matrix[row-1][col]
		else:
			# print "row and col are not 0"
			matrix[row][col] += min(matrix[row-1][col], matrix[row][col-1])
		row += 1
		col -= 1


if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time ()
	print("Solved in %.4f seconds." % (done - start))