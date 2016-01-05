import time

def main():
	triangle = []
	with open("067.txt", "r") as f:
		# Read the triangle from the file, storing it in a 2-dimensional int array
		for line in f.read().split("\n"):
			numbers_in_line = list(line.strip().split(" "))
			triangle.append([int(number) for number in numbers_in_line])

		# Apply the algorithm for traversing the triangle with the max cost
		for line in xrange(len(triangle)-1, -1, -1):
			for cell in xrange(0, len(triangle[line])-1):
				triangle[line-1][cell] = triangle[line-1][cell] + max([triangle[line][cell], triangle[line][cell+1]])

		print("The result is %d." % triangle[0][0])


if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))