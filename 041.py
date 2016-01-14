import itertools
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


def main():
	max_pandigital = 0
	digits = range(1, 10)

	for n in xrange(7, 4, -1):
		for n_digits in itertools.permutations(digits[:n]):
			string_number = "".join([str(digit) for digit in n_digits])
			pandigital_number = int(string_number)
			if is_prime(pandigital_number) and len(string_number) == n:
				max_pandigital = max(max_pandigital, pandigital_number)

	print("The result is %d." % max_pandigital)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))