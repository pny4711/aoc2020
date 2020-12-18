def is_sum_of_pair(b, e, n, v):
    for i in range(b,e-1):
        for j in range(i,e):
            if n[i] + n[j] == v:
                return True
    return False

def p1(n, p):
    for x in range(p,len(n)):
        if not is_sum_of_pair(x-p,x,n,n[x]):
            return x

def p2(n, x):
    v,s,sum = n[x], 0, 0
    for y in range(0,x):
        sum += n[y]
        while sum > v:
            sum -= n[s]
            s += 1
            if sum == v:
                return n[s:y]

preamble=25
numbers = [int(line) for line in open("input.txt")]

x = p1(numbers, preamble)
xx = p2(numbers, x)

print("Part1: %d\nPart2: %d" % (numbers[x], xx[0] + xx[-1]))
