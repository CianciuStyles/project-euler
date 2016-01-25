import time

def combinations(n, r):
	return (fact(n)) / (fact(r) * fact(n-r))

def fact(n):
	result = 1
	for i in xrange(2, n+1):
		result *= i

	return result			

def main():
	total = 0
	for a in xrange(1, 101):
		for b in xrange(1, 101):
			if combinations(a, b) > 1000000:
				total += 1

	print("The result amounts to %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))