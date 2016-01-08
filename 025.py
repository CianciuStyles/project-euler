import math
import time

def main():
	total = 2
	fib = (0, 1, 1)
	while len(str(fib[2])) < 1000:
		fib = (fib[1], fib[2], fib[1] + fib[2])
		total += 1

	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))