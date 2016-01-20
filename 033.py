import time

def main():
	fractions = set()
	for num in xrange(10, 100):
		for den in xrange(10, 100):
			# Fractions ending in 0 are considered to be trivial, so we skip them
			if num % 10 == 0 and den % 10 == 0:
				continue

			# The fractions we are looking for are less than one in value
			# so let's skip the fraction in which num is equal or more than den
			if num >= den:
				continue

			num_s = str(num)
			den_s = str(den)

			for x in xrange(0, 2):
				for y in xrange(0, 2):

					# If the digits are not the same, we can not simplify them
					if num_s[x] != den_s[y]:
						continue

					# Find the new numerator and denominator after the 'simplification'
					num2 = float(num_s[1-x])
					den2 = float(den_s[1-y])

					if den2 != 0.0 and num2 / den2 == num / float(den):
						fractions.add((num, den))

	final_fraction = (1, 1)
	for fraction in fractions:
		final_fraction = (final_fraction[0] * fraction[0], final_fraction[1] * fraction[1])

	print("The result is %d/%d." % (final_fraction[0], final_fraction[1]))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))