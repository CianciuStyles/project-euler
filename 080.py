from decimal import *

import math
import time

def main():
	getcontext().prec = 105
	result = 0

	for num in xrange(101):
		square_root = Decimal(num).sqrt()

		if round(square_root) == square_root:
			continue

		string_number = str(square_root).split(".")
		decimal_digits = string_number[0] + string_number[1][:99]
		result += sum([int(digit) for digit in decimal_digits])

	print("The result is %d." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))