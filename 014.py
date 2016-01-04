import time

collatz_chains = {1: 1}

def collatz(num):
	global collatz_chains
	if not collatz_chains.has_key(num):
		if num % 2 == 0:
			collatz_chains[num] = collatz(num / 2) + 1
		else:
			collatz_chains[num] = collatz((3 * num + 1) / 2) + 2

	return collatz_chains[num]

def main():
	max, max_collatz = 0, 0
	for num in xrange(1000000, 1, -1):
		current_num_collatz = collatz(num)
		if current_num_collatz > max_collatz:
			max_collatz = current_num_collatz
			max = num

	print("The result is %d." % max)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))