import math
import time

def main():
	# Dimension of the spiral
	dimension = 1001

	# Starting the total from 1, which represents the center of the spiral
	total = 1

	# This loop takes care of the numbers along the diagonal from top-left to bottom-right
	# Starting from the center, we have 1, 3, 7, 13, 21, ...
	# We can obtain these numbers by adding multiples of two to the last number we got
	# Example: 1 + 2 = 3, 3 + 4 = 7, 7 + 6 = 13, 13 + 8 = 21, ...
	toadd, lastnum = 2, 1
	for _ in xrange(1, dimension):
		lastnum += toadd
		total += lastnum
		toadd += 2

	# This loops takes care of the numbers along the diagonal from top-right to bottom-left
	# Starting from the center, we have 1, 5, 9, 17, 25, ...
	# We can obtain these numbers by adding multiples of 4 every other time to the last number we got
	# (the phase variable ensures we add 4 to tonum every other time)
	# Example: 1 + 4 = 5, 5 + 4 = 9, 9 + 8 = 17, 17 + 8 = 25, ...
	toadd, lastnum, phase = 4, 1, True
	for _ in xrange(1, dimension):
		lastnum += toadd
		total += lastnum
		phase = not phase
		if phase is True:
			toadd += 4

	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))