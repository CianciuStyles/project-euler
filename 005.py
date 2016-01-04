import time

def gdc(a, b):
	"""Compute the greatest common divisor using Euclid's formula (https://en.wikipedia.org/wiki/Greatest_common_divisor#Using_Euclid.27s_algorithm)"""
	while b:
		a, b = b, a % b

	return a

def lcm(a, b):
	"""Compute the least common multiple by reduction (https://en.wikipedia.org/wiki/Least_common_multiple#Reduction_by_the_greatest_common_divisor)"""
	return a * b // gdc(a, b)

def main():
	print("The result is %d." % reduce(lambda x,y : lcm(x, y), range(1, 20)))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))