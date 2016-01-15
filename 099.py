import math
import time

def main():
    with open("099.txt", "r") as f:
        lines = [line.strip() for line in f.readlines()]
        max, max_index = -1, -1
        for index, line in enumerate(lines):
            numbers = line.split(",")
            prod = int(numbers[1]) * math.log(int(numbers[0]))
            if prod > max:
                max, max_index = prod, index

        print("The result is %d." % (max_index + 1))


if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))