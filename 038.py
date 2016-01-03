import itertools
from time import time

def isPandigital(num):
   	return len(num) == 9 and set(num) == set("123456789")

def main():
	start = time()
	
	max_pandigital_number = 0

	for num in range(10000):
		sequence = str(num)
		prod = 1

		while len(sequence) < 9:
			prod += 1
			sequence = "".join((sequence, str(num*prod)))

		if len(sequence) == 9 and isPandigital(sequence):
			if int(sequence) > max_pandigital_number:
				# print "Found new max pandigital! " + sequence
				max_pandigital_number = int(sequence)

	print(max_pandigital_number)
	print("Solved in %.4f seconds." % (time() - start))

if __name__ == '__main__':
	main()