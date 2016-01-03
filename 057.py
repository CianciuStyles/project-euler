import time

def main():
	start = time.time()

	num_solutions = 0
	h = [0, 1]
	k = [1, 0]

	for iteration in range(2, 1003):
		if iteration == 2:
			a = 1
		else:
			a = 2

		current_h = a * h[iteration-1] + h[iteration-2]
		current_k = a * k[iteration-1] + k[iteration-2]

		# print("Iteration {0}: {1}/{2}".format(iteration-2, current_h, current_k))
		h.append(current_h)
		k.append(current_k)

		if len(str(current_h)) > len(str(current_k)):
			num_solutions += 1

	print("Number of solutions: {0}".format(num_solutions))
	end = time.time()
	print("Solved in %.4f seconds." % (end - start))

if __name__ == '__main__':
	main()