import math
import time

def value(name):
	total = 0
	for char in list(name):
		total += ord(char) - 64

	return total

def main():
	with open("022.txt", "r") as f:
		# Read the names from the file
		names = sorted([name[1:-1] for name in f.read().strip().split(",")])
		# print(names)

		total = 0
		for index, name in enumerate(names):
			total += (index + 1) * value(name)

		print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))