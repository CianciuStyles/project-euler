import time

def is_palindrome(number):
	return str(number) == str(number)[::-1]

def is_lychrel(number):
	iteration, partial_result = 0, number
	while iteration < 50:
		reverse = int(str(partial_result)[::-1])
		partial_result += reverse
		if is_palindrome(partial_result):
			return False
		else:
			iteration += 1

	return True

def main():
	total = 0
	for num in xrange(1, 10001):
		if is_lychrel(num):
			total += 1

	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))