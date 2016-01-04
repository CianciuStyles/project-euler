import time

def catalan_number(num):
	return factorial(2 * num) / (factorial(num) ** 2)

def factorial(num):
	fact = 1
	while 1 <= num:
		fact *= num
		num -= 1

	return fact

def main():
	# The number of paths of monotonic lattice paths in a NxN grid is given by the N-th Catalan number
	# https://en.wikipedia.org/wiki/Catalan_number#Applications_in_combinatorics
	print("The result is %d." % catalan_number(20))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))