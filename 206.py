import math
import time

def check_number(array):
	return (array[0] == '1' and array[2] == '2' and array[4] == '3' and
			array[6] == '4' and array[8] == '5' and	array[10] == '6' and
			array[12] == '7' and array[14] == '8' and array[16] == '9')
def main():
	min, max = int(math.sqrt(10203040506070809)), int(math.sqrt(19293949596979899))
	number = min - (min % 10) + 3
	result = ""

	while number < max:
		array = str(number * number)
		if check_number(array):
			result = array
			break

		number += 4
		array = str(number * number)
		if check_number(array):
			result = array
			break

		number += 6

	result = math.sqrt(int(result)) * 10
	print("The result amounts to %d." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))