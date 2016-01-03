import time

def main():
	total = 0
	
	# For all the number between 1 and 1000...
	for num in range(1, 1000):
		# Check if the number is divisible by 3 or by 5
		if num % 5 is 0 or num % 3 is 0:
			total += num

	print("The sum amounts to %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))