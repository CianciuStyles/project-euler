import itertools
import time

prime_factors = {}

def factorize(n):
	if prime_factors.has_key(n) == False:
		prime_factors[n] = set([n])
		for d in xrange(2, int(n ** 0.5)+1):
			if n % d == 0:
				prime_factors[n] = prime_factors[n // d] | set([d])
				break
	return len(prime_factors[n])

def main():
	for i in itertools.count(2):
		if map(factorize, range(i, i+4)) == [4, 4, 4, 4]:
			result = i
			break

	print("The result is %d." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))