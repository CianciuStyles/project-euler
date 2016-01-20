import time

def main():
	target = 200
	currencies = [1, 2, 5, 10, 20, 50, 100, 200]
	numWays = []

	for i in xrange(0, len(currencies)):
		for j in xrange(currencies[i], target+1):
			numWays.append(0)
	numWays[0] = 1

	for i in xrange(0, len(currencies)):
		for j in xrange(currencies[i], target+1):
			numWays[j] += numWays[j - currencies[i]]

	print("The result is %d." % numWays[target])

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))