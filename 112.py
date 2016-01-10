import time

def is_bouncy(number):
	digits = [int(digit) for digit in str(number)]
	increasing = decreasing = True
	for index in xrange(0, len(digits) - 1):
		if digits[index] > digits[index + 1]:
			increasing = False
		if digits[index] < digits[index + 1]:
			decreasing = False

		if increasing is False and decreasing is False:
			return True

	return False

def main():
	result = 0
	num, proportion, bouncy_numbers = 100, 0, 0
	while True:
		bouncy_numbers += 1 if is_bouncy(num) else 0
		proportion = bouncy_numbers * 100 / num
		
		if proportion == 99 and bouncy_numbers * 100 % num == 0:
			result = num
			break

		num += 1

	print("The result is %d." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))