import itertools
import math
import time

def num_divisors(num):
	factors = 0
	for x in xrange(1, int(math.sqrt(num) + 1)):
		if num % x == 0:
			factors += 2

	return factors

def main():
	num = 0
	for i in itertools.count():
		num += i
		if num_divisors(num) > 500:
			print("The result is %d." % num)
			return

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))