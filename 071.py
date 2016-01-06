import time

def main():
	# Implemented the insight from http://math.stackexchange.com/a/39595
	last_numerator = 0
	for den in xrange(1, 1000001):
		num = ((3 * den) - 1) / 7.0
		if num.is_integer():
			last_numerator = num

	print("The result is %d." % last_numerator)


if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))