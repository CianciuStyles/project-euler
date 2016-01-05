import itertools
import time

def main():
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	for index, permutation in enumerate(itertools.permutations(numbers)):
		if index == 999999:
			print("The result is %s." % "".join(permutation))


if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))