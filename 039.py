import collections
import time

def multiply_matrices(matrix, col):
	'''Multiplies a 2x2 matrix with a 2x1 column vector, resulting in a 2x1 column vector'''
	return [matrix[0][0] * col[0] + matrix[0][1] * col[1],
	        matrix[1][0] * col[0] + matrix[1][1] * col[1]]

def main():
	# The idea for solving this problem is taken from https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples#Alternative_methods_of_generating_the_tree
	target = 1000 # This is the upper bound for the parameters
	triples = [] 

	# These values will generate all the Pythagorean triples according
	# to the formula in the Wikipedia article mentioned above
	initialUV = [3, 1]
	triples.append(initialUV)
	matrices = [
		[(2, -1), (1, 0)],
		[(2, 1),  (1, 0)],
		[(1, 2),  (0, 1)]
	]

	# In this loop all the Pythagorean triples are generated,
	# and the sums defaultdict will keep track of how many times
	# a certain perimeter has been generated
	sums = collections.defaultdict(lambda: 0)
	for index in xrange(0, 501):
		for matrix in matrices:
			triples.append(multiply_matrices(matrix, triples[index]))

			u, v = triples[index]
			a, b, c = u * v, (u ** 2 - v ** 2)/2, (u ** 2 + v ** 2)/2

			kth_sum = a + b + c
			while kth_sum <= target:
				sums[kth_sum] += 1
				kth_sum += a + b + c

	# We filter the sums dictionary to contain only the (key, value)
	# pairs for which the value is below the target
	sums = {k:v for (k, v) in sums.iteritems() if v <= target}

	# We look for the final result of the problem, keeping the value
	# that generates the maximum number of solutions
	result, max_value = 0, 0
	for (current_key, current_value) in sums.iteritems():
		if current_value > max_value:
			result, max_value = current_key, current_value

	print("The result is %d." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))