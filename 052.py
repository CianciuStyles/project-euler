import time

def same_digits(x, y):
	c = sorted([int(digit) for digit in str(x)])
	d = sorted([int(digit) for digit in str(y)])

	return c == d

def main():
	num = 10
	while True:
		x2, x3, x4, x5, x6 = num*2, num*3, num*4, num*5, num*6
		if same_digits(num, x2) and same_digits(num, x3) and same_digits(num, x4) and same_digits(num, x5) and same_digits(num, x6):
		   result = num
		   break

		num += 1

	print("The result is %d." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))