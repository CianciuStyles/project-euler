import itertools
from time import time

def main():
	start = time()

	results = []
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	for permutation in list(itertools.permutations(numbers)):
		for product_index in range(4, 9):
			# print "Product Index: %d" % product_index
			for equals_index in range(product_index+1, 9):
				# print "Equals Index: %d" % equals_index
				product      = int("".join(permutation[0:product_index]))
				multiplier   = int("".join(permutation[product_index:equals_index]))
				multiplicand = int("".join(permutation[equals_index:]))

				# print "Checking %d x %d = %d" % (multiplicand, multiplier, product)
				if multiplicand * multiplier == product:
					# print "%d x %d = %d" % (multiplicand, multiplier, product)
					if product not in results:
						results.append(product)

	result = 0
	for res in results:
		result += res

	print(result)
	print("Solved in %d seconds." % (time() - start))

if __name__ == '__main__':
	main()