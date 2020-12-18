
# inp = [ 0,3,6 ]

inp = [16,11,15,0,1,7]

# Given the starting numbers 1,3,2, the 2020th number spoken is 1.
# Given the starting numbers 2,1,3, the 2020th number spoken is 10.
# Given the starting numbers 1,2,3, the 2020th number spoken is 27.
# Given the starting numbers 2,3,1, the 2020th number spoken is 78.
# Given the starting numbers 3,2,1, the 2020th number spoken is 438.
# Given the starting numbers 3,1,2, the 2020th number spoken is 1836.
# Given your starting numbers, what will be the 2020th number spoken?

# Your puzzle input is 16,11,15,0,1,7.

m = {}
t = 0
for i in inp:
    t += 1
    m[i] = (t, t)

l = inp[-1]

while t < 30000000:
    t += 1
    x0,x1 = m[l]
    l = x1 - x0
    if t == 2020:
        print("%10d   %d" % (t, l))
    if l in m:
        _, xl1 = m[l]
    else:
        xl1 = t
    m[l] = (xl1, t)

print("%10d   %d" % (t, l))
