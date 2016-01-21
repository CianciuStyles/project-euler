import time

def main():
	string = ""
	for i in xrange(1, 1000001):
		string += str(i)

	total = int(string[0])
	total *= int(string[9])
	total *= int(string[99])
	total *= int(string[999])
	total *= int(string[9999])
	total *= int(string[99999])

	print("The result is %d." %  total)

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))