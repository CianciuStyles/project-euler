import time

def main():
	max_sum = 0
	for a in xrange(1, 101):
		for b in xrange(1, 101):
			number = a ** b
			sum_of_digits = sum([int(digit) for digit in str(number)])
			max_sum = max(max_sum, sum_of_digits)

	print("The result is %d." % max_sum)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))