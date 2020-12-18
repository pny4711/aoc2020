
numbers = [int(l) for l in open("inputx.txt")]

print([(x*y, x, y) for x in numbers for y in numbers if x + y == 2020][0])
print([(x*y*z, x, y,z) for x in numbers for y in numbers for z in numbers if x + y + z == 2020][0])



