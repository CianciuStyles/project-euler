import time

def largest_prime_factor(n):
	i = 2
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
	return n

def main():
	print("The result is %d." % largest_prime_factor(600851475143))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))