import itertools
import time

def is_circular(num):
	rotations = rotate(num)
	rotations.add(int(num))
	result = True
	for rot in rotations:
		if is_prime(rot) == False:
			result = False

	return result

def rotate(num):
	result = set()
	result.add(int(num))
	my_num = num[:]

	for _ in xrange(1, len(num)+1):
		num = num[-1:] + num[:-1]
		if num == my_num:
			break
		result.add(num)

	return result

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

    # range starts with 3 and only needs to go up 
    # the square root of n for all odd numbers
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

def main():
	circular_primes = set([2, 3, 5, 7])
	for length in xrange(2, len("1000000")):
		primes = ["".join(prime) for prime in itertools.product(['1', '3', '7', '9'], repeat=length)]
		for prime in primes:
			if is_prime(prime) and is_circular(prime):
				circular_primes.add(int(prime))

	print("The result is %d." % len(circular_primes))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))