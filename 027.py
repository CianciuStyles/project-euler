import time

def primes_up_to(num):
	# This function is taken from http://stackoverflow.com/a/568618
	D, q, primes = {}, 2, set()
	while q < num:
		if q not in D:
			primes.add(q)
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]
		q += 1

	return primes

def main():
	primes = primes_up_to(50000)
	max_consecutive_primes, max_product = 0, 0
	max_product = 0
	for a in xrange(-1000, 1001, 1):
		for b in xrange(-1000, 1001, 1):
			is_prime, n, current_consecutive_primes = True, 0, 0
			while is_prime == True:
				if (n ** 2 + a * n + b) in primes:
					current_consecutive_primes += 1
				else:
					is_prime = False
				n += 1

			if current_consecutive_primes > max_consecutive_primes:
				max_consecutive_primes = current_consecutive_primes
				max_product = a * b
	print("The sum amounts to %d." % max_product)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))