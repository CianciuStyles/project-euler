import time

def main():
	digits = [int(digit) for digit in list(str(2 ** 1000))]
	total = sum(digits)
	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))