import time

def is_palindrome(num):
	return str(num) == str(num)[::-1]

def main():
	max_product, max_x, max_y = 0, 0, 0
	for x in range(999, 1, -1):
		for y in range(x, 1, -1):
			product = x * y
			if is_palindrome(product) and product > max_product:
				max_x, max_y, max_product = x, y, product
				
	print("The result is %d*%d = %d." % (max_x, max_y, max_product))

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()
	print("The solution took %.4f seconds to compute." % (done - start))