import time

def factorial(num):
	fact = 1
	while 1 <= num:
		fact *= num
		num -= 1

	return fact

def sum_factorial(number):
	digits = [int(digit) for digit in str(number)]
	total = 0
	for digit in digits:
		total += factorial(digit)

	return total

def main():
	total = 0
	for num in xrange(3, 50001):
		if sum_factorial(num) == num:
			total += num

	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))