import time

def nth_prime_number(num):
	# This function is taken from http://stackoverflow.com/a/568618
	D, q, primes = {}, 2, []
	while len(primes) < num:
		if q not in D:
			primes.append(q)
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]
		q += 1

	return primes[-1]

def main():
	print("The result is %d." % nth_prime_number(10001))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))