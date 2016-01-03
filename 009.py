import time

def main():
	# The Euclid's formula for generating Pythagorean triplets is taken from https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
	for m in range(1, 501):
		for n in range(m, 501):
			a, b, c = (2 * m * n), (n ** 2 - m ** 2), (n ** 2 + m ** 2)

			if a + b + c == 1000:
				print("The product amounts to %d." % (a*b*c))


if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))