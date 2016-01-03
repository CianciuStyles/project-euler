from math import sqrt
from itertools import count, islice
from time import time

def count_primes(list):
	primes = [num for num in list if is_prime_number(num)]
	return len(primes)

def is_prime_number(n):
    if n < 2:
    	return False

    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def main():
	start = time()

	num_primes = 0
	num_diagonal_numbers = 1

	for n in range(3, 100000, 2):
		current_diagonal_numbers = []
		
		for m in range((n-2)**2, n**2+1, n-1):
			current_diagonal_numbers.append(m)

		current_diagonal_numbers = current_diagonal_numbers[1:]

		num_primes += count_primes(current_diagonal_numbers)
		num_diagonal_numbers += 4

		ratio = float(num_primes) / num_diagonal_numbers
		# print("The ratio for {3} is {0}/{1} = {2}".format(num_primes, num_diagonal_numbers, ratio, n))
		
		if ratio < 0.10:
			answer = n
			break

	print("The answer is {0}.".format(answer))
	print("It took {0} seconds to compute.".format(float(time()-start)))

if __name__ == '__main__':
	main()