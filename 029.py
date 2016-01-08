import time

def main():
	array = set()
	for a in xrange(2, 101):
		for b in xrange(2, 101):
			array.add(a ** b)

	print("The result is %d." % len(array))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))