import time

def main():
	# Generate a set of triangular numbers
	triangular_numbers = set([n * (n - 1) / 2 for n in range(286, 100001)])

	# Generate a set of pentagonal numbers
	pentagonal_numbers = set([n * (3*n - 1) / 2 for n in range(165, 100001)])

	# Generate a set of hexagonal numbers
	hexagonal_numbers = set([n * (2*n - 1) for n in range(165, 100001)])

	# Find the number which is simultaneously triangular, pentagonal and hexagonal
	result = hexagonal_numbers.intersection(pentagonal_numbers.intersection(triangular_numbers))
	print("The result is %d." % result.pop())

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))