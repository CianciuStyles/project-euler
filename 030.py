import time

def sum_fifth_power(num):
	return sum([int(digit) ** 5 for digit in list(str(num))])

def main():
	total = 0
	for num in xrange(2, 1000001):
		if num == sum_fifth_power(num):
			total += num

	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))