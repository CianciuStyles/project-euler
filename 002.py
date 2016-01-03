import time

def main():
	total = 0
	fib = (0, 1, 1)

	# Until the last calculated Fibonacci term's value is under 4 million...
	while fib[2] < 4000000:
		# Calculate the new Fibonacci term
		fib = (fib[1], fib[2], fib[1] + fib[2])

		# Check if it is even
		if fib[2] % 2 is 0:
			total += fib[2]

	print("The sum amounts to %d." % total)


if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))