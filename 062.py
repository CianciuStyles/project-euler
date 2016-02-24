import collections
import time

def main():
	current_number = 345 # The number from which we will start our search

	# We will maintain two auxiliay data structures for solving this problem:
	# 1. A default dict which will contain how many cubes share the same digits (i. e., are permutations of the same number)
	cubes_with_the_same_digits = collections.defaultdict(int)
	# 2. A dict that tells us which is the lowest number that generates an entry in the defaultdict discussed above
	lowest_number_generating_the_cube = dict()

	while True:
		# We get a string containing the sorted digits of the cube we are generating
		# So that permutations of the same digits will access the same key in the default dict
		sorted_list = "".join(sorted(str(current_number ** 3)))

		# If the default dict tells us that no such string has been encountered before,
		# this means that current_numer is the lowest cube that generates those digits
		# so we store it in the second dict
		if cubes_with_the_same_digits[sorted_list] == 0:
			lowest_number_generating_the_cube[sorted_list] = current_number

		# We keep track of the fact that we generated a cube with a certain set of digits
		cubes_with_the_same_digits[sorted_list] += 1

		# The first set of digits that reaches the value 5 (i. e., has five numbers whose
		# cubes generate the same set of digits) is corresponding to the lowest cube we were looking for
		if cubes_with_the_same_digits[sorted_list] == 5:
			result = lowest_number_generating_the_cube[sorted_list]
			break

		current_number += 1

	print("The result is %d." % result ** 3)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))