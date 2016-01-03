import time

def main():
	start_time = time.time()
	chain_end = dict()
	next_number = dict()
	end_in_1 = 0
	end_in_89 = 0

	for number in range(1, 10000000):
		current_chain = [number]

		while number != 1 and number != 89:
			try:
				number = chain_end[number]
			except KeyError:
				try:
					number = next_number[number]
					current_chain.append(number)
				except KeyError:
					next_number[number] = sum(x*x for (x) in map(int, str(number)))
					number = next_number[number]
					current_chain.append(number)

		if number == 1:
			for chain in current_chain:
				chain_end[chain] = 1
			end_in_1 +=1
		else:
			for chain in current_chain:
				chain_end[chain] = 89
			end_in_89 +=1

		# print("{0} terminates in {1}".format(original_number, number))

	print("How many numbers end their chain in 89? {0}".format(end_in_89))
	end_time = time.time()
	print("Calculated in %.4f seconds" % (end_time-start_time))

if __name__ == '__main__':
	main()