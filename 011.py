import time

def check_vertical(matrix):
	max_product = 0

	for row in xrange(0, len(matrix)-3):
		for col in xrange(0, len(matrix)):
			product = matrix[row][col] * matrix[row+1][col] * matrix[row+2][col] * matrix[row+3][col]
			max_product = max(product, max_product)

	return max_product

def check_horizontal(matrix):
	max_product = 0

	for row in xrange(0, len(matrix)):
		for col in xrange(0, len(matrix)-3):
			product = reduce(lambda x,y: x*y, matrix[row][col:col+3])
			max_product = max(product, max_product)

	return max_product

def check_left_diagonal(matrix):
	max_product = 0

	for row in xrange(0, len(matrix)-3):
		for col in xrange(0, len(matrix)-3):
			product = matrix[row][col] * matrix[row+1][col+1] * matrix[row+2][col+2] * matrix[row+3][col+3]
			max_product = max(product, max_product)

	return max_product

def check_right_diagonal(matrix):
	max_product = 0

	for row in xrange(0, len(matrix)-3):
		for col in xrange(0, len(matrix)-3):
			product = matrix[row+3][col] * matrix[row+2][col+1] * matrix[row+1][col+2] * matrix[row][col+3]
			max_product = max(product, max_product)

	return max_product

def main():
	with open("011.txt", "r") as f:
		# Read the matrix from the text file, and store in an integet 2-dimensional array
		matrix = []
		for line in f.readlines():
			matrix.append([int(num) for num in line.split(" ")])
		# print matrix

		# Check the matrix along the various directions, and find the max product of four adjacent numbers
		print("The result is %d." % max(check_vertical(matrix), check_horizontal(matrix), check_left_diagonal(matrix), check_right_diagonal(matrix)))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))