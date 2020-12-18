
import math

def check_slope(lines, right, down):
	offset = 0
	trees = 0
	part_down = 0

	for line in lines:
		if part_down:
			part_down -= 1
		else:
			if offset >= len(line):
				offset -= len(line)
			if line[offset] == '#':
				trees += 1
			offset += right
			part_down = down - 1
	return trees

all_lines = [line.strip() for line in open("input.txt")]

prod = 1
for r, d in ((1,1),(3,1),(5,1),(7,1),(1,2)):
	t = check_slope(all_lines, r, d)
	prod *= t
	print("- Right %d, down %d: %d" % (r, d, t))

# prod2 = math.prod([ check_slope(all_lines, r, d) for r, d in ((1,1),(3,1),(5,1),(7,1),(1,2))])

print("  Product: %d" % prod)
# print("  Product2: %d" % prod2)