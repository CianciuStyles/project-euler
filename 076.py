import datetime
import math
import time

partitions = dict()

def p(number):
	return partition(number, number)

def partition(n, m):
	global partitions

	if n <= 1: # Recursive stopping condition
		return 1

	if m > n:
		return partition(n, n)

	if (n, m) in partitions:
		return partitions[(n, m)]

	total = 0
	for k in xrange(1, m + 1):
		total += partition(n - k, k)

	partitions[(n, m)] = total
	return total

def main():
	# The insight for this problem has been taken from https://en.wikipedia.org/wiki/Partition_%28number_theory%29#Algorithm
	print("The result is %d." % (p(100) - 1))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))