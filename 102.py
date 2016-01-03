import time

def main():
	# Read triples of points
	input_text = open("Euler 102.txt", "r")
	triangles = []
	for line in input_text.readlines():
		coords = line.split(",")
		first_point  = (int(coords[0]), int(coords[1]), 0)
		second_point = (int(coords[2]), int(coords[3]), 0)
		third_point  = (int(coords[4]), int(coords[5]), 0)
		triangles.append([first_point, second_point, third_point])
	# print triangles

	# Test each triangle if it contains the origin
	sum = 0
	for triangle in triangles:
		if check_same_side(triangle):
			sum += 1

	print(sum)

def check_same_side(triangle):
	A, B, C = triangle[0], triangle[1], triangle[2]

	if same_side(A, B, C) and same_side(B, A, C) and same_side(C, A, B):
		return True
	else:
		return False

def same_side(point1, point2, point3):
	cp1 = cross_product((point2[0]-point3[0], point2[1]-point3[1], 0), (-point2[0], -point2[1], 0))
	cp2 = cross_product((point2[0]-point3[0], point2[1]-point3[1], 0), (point1[0]-point2[0], point1[1]-point2[1], 0))
	if dot_product(cp1, cp2) >= 0:
		return True
	else:
		return False

def cross_product(vec1, vec2):
	s1 = vec1[1]*vec2[2] - vec1[2]*vec2[1]
	s2 = vec1[2]*vec2[0] - vec1[0]*vec2[2]
	s3 = vec1[0]*vec2[1] - vec1[1]*vec2[0]

	return (s1, s2, s3)

def dot_product(vec1, vec2):
	assert(len(vec1) == len(vec2))

	product = 0
	for idx in range(len(vec1)):
		product += vec1[idx] * vec2[idx]

	return product

if __name__ == '__main__':
	start = time.time()
	main()
	done = time.time()

	print("Solved in %.4f seconds." % (done - start))