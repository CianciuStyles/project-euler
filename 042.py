import time

def triangular_numbers_up_to(upper_bound):
	triangular_numbers = []
	for num in range(1, upper_bound+1):
		triangular_numbers.append(num * (num + 1) / 2)
	return triangular_numbers

def main():
	with open("042.txt", "r") as f:
		# Generate an array of triangular numbers
		triangular_numbers = triangular_numbers_up_to(100)

		# Read the names from the file, strip the double quotes and populate an array out of them
		names = f.read().replace('\"', ''). split(',')

		# Number of triangular words (to be found)
		result = 0

		for name in names:
			# Calculate the sum of the letters in the name
			total = 0
			for letter in name:
				total += ord(letter) - ord('A') + 1

			# If the sum is a triangular number, add one to the result
			result += 1 if total in triangular_numbers else 0

	print("The result is %d." % result)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))