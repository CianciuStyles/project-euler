import time

def factorial(num):
	if num == 0:
		return 1
	else:
		return num * factorial(num - 1)

def main():
	digits_list = [int(digit) for digit in list(str(factorial(100)))]
	print("The result is %d." % sum(digits_list))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))