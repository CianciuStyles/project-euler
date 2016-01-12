import time

def main():
	total = 0
	for num in xrange(1, 1001):
		total += num ** num

	last_ten_digits = "".join(str(total)[-10:])
	print("The result is %s." % last_ten_digits)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))