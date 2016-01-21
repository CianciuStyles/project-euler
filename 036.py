import time

def is_palindrome(string):
	return string == string[::-1]

def main():
	total = 0
	for num in xrange(1, 1000001):
		if is_palindrome(str(num)) and is_palindrome(bin(num)[2:]):
			total += num

	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))