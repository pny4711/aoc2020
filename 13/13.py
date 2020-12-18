
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

#-----8<-------------------------------------

# def verify(t, a):
#    print("verify %d with %s" % (t, str(a)))
#    for x, nr in a:
#        if t % x != (-nr % x):
#            print("Fail: %d %% %d = %d" % (t, x, t % x))

a = [line for line in open("input.txt")]

#a[1] = '17,x,13,19'
b = [int(n) for n in a[1].split(',') if n !='x']
b2 = [(int(x), n) for n, x in enumerate(a[1].split(',')) if x !='x']
t = int(a[0])

best = t
bestb = 0

# print(t)

for bb in b:
    d = ((1 + int((t - 1) // bb)) * bb) - t
    if d < best:
        best = d
        bestb = bb

a_s = [ x-(n%x) for x, n in b2 ]
n_s = [ x for x,_ in b2 ]

part2 = chinese_remainder(n_s, a_s)
# verify(chr, b2)

print("Part1: %d" % (best * bestb))
print("Part2: %d" % part2)
