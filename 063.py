import math

def main():
	counter = 0
	for power in range(1, 25):
		for i in range(1, 100):
			n = i ** power
			if len(str(n)) == power:
				print(str(i) + " ** " + str(power) + " = " + str(n))
				counter += 1

	print(counter)

if __name__ == '__main__':
	main()