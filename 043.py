import itertools
import time

def main():
	digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	total = 0
	
	for permutation in itertools.permutations(digits):
		if (int(permutation[1]+permutation[2]+permutation[3]) % 2 == 0 and
			int(permutation[2]+permutation[3]+permutation[4]) % 3 == 0 and
			int(permutation[3]+permutation[4]+permutation[5]) % 5 == 0 and
			int(permutation[4]+permutation[5]+permutation[6]) % 7 == 0 and
			int(permutation[5]+permutation[6]+permutation[7]) % 11 == 0 and
			int(permutation[6]+permutation[7]+permutation[8]) % 13 == 0 and
			int(permutation[7]+permutation[8]+permutation[9]) % 17 == 0):
			total += int("".join(permutation))

	print("The result amounts to %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))