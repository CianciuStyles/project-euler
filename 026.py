import math
import time

def generate_primes_up_to(max_prime):
	"""Generates an array of prime numbers up to @max_prime"""
	primes = [2, 3]

	i = 4
	while i < max_prime:
		prime = True
		for divisor in xrange(2, int(math.sqrt(i)) + 1):
			if i % divisor == 0:
				prime = False
				break

		if prime is True:
			primes.append(i)

		i += 1

	return primes

def period(num):
	if num == 2 or num == 5:
		return 0

	i = 1
	while (10 ** i - 1) % num != 0:
		i += 1

	return i

def main():
	# We are looking at the fractions with prime denominators other than 2 and 5
	# because they are guaranteed to produce a repeating decimal. The length of the
	# repetend of 1/p is equal to the order of 10 modulo p.
	# See https://en.wikipedia.org/wiki/Repeating_decimal#Fractions_with_prime_denominators
	
	primes = generate_primes_up_to(1000)

	answer, max_period = 0, 0
	for prime in primes:
		current_period = period(prime)
		if current_period > max_period:
			max_period, answer = current_period, prime

	print("The result is %d." % answer)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))