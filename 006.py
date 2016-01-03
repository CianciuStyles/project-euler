import time

def main():
	sum_of_squares, sum = 0, 0

	# For all the numbers in the range 1 to 100 (included)...
	for x in range(1, 101):
		sum_of_squares += x ** 2
		sum += x

	square_of_sum = sum ** 2
	print("The difference amounts to %d." % (square_of_sum - sum_of_squares))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))