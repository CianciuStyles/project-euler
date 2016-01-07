import math
import time

def n(num):
	total = 0
	for m in xrange(1, int(math.sqrt(num)) + 1):
		if num % m == 0:
			total += m + num / m

	return total - num

def main():
	total = 0
	for num in xrange(1, 10001):
		i = n(num)
		if n(i) == num:
			if i != num:
				total += i

	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))