import time

def primes_up_to(num):
	# This function is taken from http://stackoverflow.com/a/568618
	D, q, primes = {}, 2, []
	while q < num:
		if q not in D:
			primes.append(q)
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]
		q += 1

	return primes

def same_digits(num1, num2, num3):
	return set(str(num1)) == set(str(num2)) and set(str(num2)) == set(str(num3))

def all_in_primes(num1, num2, num3, array):
	return num1 in array and num2 in array and num3 in array

def main():
	results, primes_array = [], primes_up_to(10000)
	first_num, max_num, gap = 1000, 9999, 3330
	while first_num < max_num - 2 * gap:
		second_num = first_num + gap
		third_num = second_num + gap
		if all_in_primes(first_num, second_num, third_num, primes_array) and same_digits(first_num, second_num, third_num):
			results.append("".join([str(first_num), str(second_num), str(third_num)]))

		first_num += 1

	print("The result is %s." % results[1])

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))