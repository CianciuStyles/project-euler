import time

def main():
	with open("008.txt", "r") as f:
		# Read the digits from the file and store them in a list of integers
		digits = [int(digit) for digit in list(f.read())]

		# Scan the whole list to find the thirteen adjacent digits with the greatest product
		num_of_adjacent_digits, max_product = 13, 0
		for num in range(0, len(digits) - num_of_adjacent_digits):
			nums = digits[num:num + num_of_adjacent_digits]
			product = reduce(lambda x, y: x * y, nums, 1)
			if product > max_product:
				max_product = product

		print("The greatest product is %d." % max_product)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))