import math
import time

def mod_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if (exponent % 2 == 1):
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus

    return result

def main():
    big_number = 28433 * mod_pow(2, 7830457, 10 ** 10) + 1
    print("The result is %s." % str(big_number)[-10:])


if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))