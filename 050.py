import time

def is_prime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def primes_up_to(num):
	# This function is taken from http://stackoverflow.com/a/568618
	D, q, primes = {}, 2, []
	while q < num:
		if q not in D:
			primes.append(q)
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]
		q += 1

	return primes

def main():
	primes = primes_up_to(1000000)

	sums = [0]
	partial_sum = 0
	for prime in primes:
		partial_sum += prime
		if partial_sum >= 1000000:
			break
		sums.append(partial_sum)

	max_terms, result = 0, 0
	for i in xrange(0, len(sums)):
		for j in xrange(0, i):
			if is_prime(sums[i] - sums[j]) and (i-j) > max_terms:
				max_terms = i - j
				result = sums[i] - sums[j]

	print("The result is %d." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))