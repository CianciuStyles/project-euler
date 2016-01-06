import itertools
import time

def main():
	with open("059.txt", "r") as f:
		# Read the encrypted ASCII codes from the file
		encrypted_ascii_codes = [int(digit) for digit in f.read().strip().split(",")]
		# print(encrypted_ascii_codes)

		# Variables to store the decrypted ASCII code from the key that yields the maximum number of spaces in the plaintext
		max_number_of_spaces, target_ascii_codes = 0, []

		# Try XORing the encrypted ASCII codes with all the possible combinations of three lowercase letters
		# The letters a to z are represented in ASCII within the range range 97 to 122 (hence the range(97, 123) in the code)
		for possible_key in itertools.product(range(97, 123), repeat=3):
			decrypted_ascii_codes = []
			for index, ascii_code in enumerate(encrypted_ascii_codes):
				decrypted_ascii_codes.append(ascii_code ^ possible_key[index % 3])

			# We count how many space characters (which we assume to be the most frequent character in the plaintext)
			# result from the decoded plaintext. The ASCII code for the space character is 32
			number_of_spaces = decrypted_ascii_codes.count(32)

			if number_of_spaces > max_number_of_spaces:
				max_number_of_spaces = number_of_spaces
				target_ascii_codes = decrypted_ascii_codes

		# When we have completed the search and found the decription key, let's add the resulting ASCII codes as requested
		print("The result is %d." % sum(target_ascii_codes))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))