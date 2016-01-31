import time

prime_factors = {}

def divisor_sum(n):
	if n < 2:
		return 1

	total = 0
	for div in xrange(1, int(n ** 0.5)+1):
		if n % div == 0:
			total += div
			if n / div != div:
				total += n / div


	return total - n

def main():
	limit = 28123
	abundant_nums = set(i for i in range(1, limit+1) if divisor_sum(i) > i)
	non_abundant_nums = set()

	for i in range(1, limit+1):
		if not any(i-a in abundant_nums for a in abundant_nums):
			non_abundant_nums.add(i)

	print("The result is %d." % sum(non_abundant_nums))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))