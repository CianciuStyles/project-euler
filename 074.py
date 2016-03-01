import collections
import time

# Since we have a limited number of digits, it's faster to store directly the result
# of the factorial function calculated on each of the possible outcomes
factorials = {
	"0": 1,
	"1": 1,
	"2": 2,
	"3": 6,
	"4": 24,
	"5": 120,
	"6": 720,
	"7": 5040,
	"8": 40320,
	"9": 362880
}

def sum_of_factorial_of_digits(num):
	global factorials
	return sum([factorials[digit] for digit in str(num)])

def main():
	# These are the parameters of this particular problem, extracted 
	# so to be easily changed for other instances of the same problem
	upper_limit, num_of_non_repeating_terms = 1000000, 60

	# result will contain the number of chains that contain exactly 60 non-repeating terms,
	# while each key of lenghts will contain the length of the chain leading to a repetition
	result, lengths = 0, collections.defaultdict(int)

	for num in xrange(upper_limit):
		# terms will contain the list of the terms encountered so far, in order of appearance
		# chain_lenght will store the length of the current chain starting from num
		terms, chain_length = [], 0

		while num not in terms:
			terms.append(num)
			chain_length += 1
			num = sum_of_factorial_of_digits(num)

			# If we encounter a number for which we already know how long will the generated
			# chain be, we skip the following calculations and simply add the length
			if num in lengths:
				chain_length += lengths[num]
				break

		if chain_length == num_of_non_repeating_terms:
			result += 1

		# Here we update the lengths defauldict with the chain lengths just found,
		# so to hopefully speed up following computations
		for index in xrange(len(terms)-1):
			lengths[terms[index]] = chain_length
			chain_length -= 1

	print("The result is %d." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))