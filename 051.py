import time

def getPattern5():
	return [[1, 0, 0, 0, 1],
			[0, 1, 0, 0, 1],
			[0, 0, 1, 0, 1],
			[0, 0, 0, 1, 1]]

def getPattern6():
	return [[1, 1, 0, 0, 0, 1],
			[1, 0, 1, 0, 0, 1],
			[1, 0, 0, 1, 0, 1],
			[1, 0, 0, 0, 1, 1],
			[0, 1, 1, 0, 0, 1],
			[0, 1, 0, 1, 0, 1],
			[0, 1, 0, 0, 1, 1],
			[0, 0, 1, 1, 0, 1],
			[0, 0, 1, 0, 1, 1],
			[0, 0, 0, 1, 1, 1]]

def generateNumbers(pattern, numDigits):
	'''generate new numbers by replacing part of the number (not necessarily adjacent digits) with the same digit'''
	numbers = []
	for i in range(10):
		if pattern[0] == 0 and i == 0:
			continue

		nIdx, num = 0, []
		for p in pattern:
			if p == 1:
				num.append(numDigits[nIdx])
				nIdx += 1
			else:
				num.append(i)
		numbers.append("".join([str(digit) for digit in num]))
	return numbers

def is_prime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def main():
	for num in range(11, 1000, 2):
		if num % 5 == 0:
			continue

		digits = [int(digit) for digit in str(num)]
		for pattern in getPattern5() if num < 100 else getPattern6():
			numbers = generateNumbers(pattern, digits)

			size = len(numbers)
			for number in numbers:
				if not is_prime(number):
					size -= 1
					if size < 8:
						break

			if size == 8:
				result = numbers[0]

	print("The result is %s." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))