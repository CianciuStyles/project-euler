import sys
import time

def pentagonal_number_up_to(number):
	pentagonal_numbers = set()
	for num in xrange(1, number + 1):
		pentagonal_numbers.add((num * (3 * num - 1)) / 2)

	return pentagonal_numbers

def main():
	pentagonal_numbers = pentagonal_number_up_to(5000)
	miniumum_difference = sys.maxsize
	for x in pentagonal_numbers:
		for y in pentagonal_numbers:
			if (x + y) in pentagonal_numbers and (x - y) in pentagonal_numbers:
				miniumum_difference = min(miniumum_difference, abs(x-y))
	print("The result is %d." % miniumum_difference)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))