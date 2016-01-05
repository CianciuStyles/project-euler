import time

def number_to_words(num):
	units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
	tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
	result = ""

	while num > 0:
		# Handle one thousand
		if num == 1000:
			result += "onethousand"
			break

		# Handle the hundreds
		elif num >= 100:
			quotient = num % 100
			result += units[(num - quotient) / 100] + "hundred"
			result += "and" if quotient > 0 else ""
			num = quotient

		# Handle the tens (with the exception of 10-20)
		elif num >= 20:
			quotient = num % 10
			result += tens[(num - quotient) / 10 - 2]
			num = quotient

		# Handle the units (and 10-20)
		elif num >= 0:
			result += units[num]
			num = 0

	return result

def main():
	
	total = 0
	for num in xrange(1, 1001):
		total += len(number_to_words(num))

	print("The result is %d." % total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))