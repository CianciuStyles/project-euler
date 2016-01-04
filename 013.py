import time

def main():
	with open("013.txt", "r") as f:
		total = 0
		for line in f.readlines():
			total += int(line)

		# Check the matrix along the various directions, and find the max product of four adjacent numbers
		print("The result is %s." % str(total)[0:9])

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))