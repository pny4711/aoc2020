ss = [1] + [ sum([format(i,"0%db" % (n)).find('000') == -1 for i in range(1<<n)]) for n in range(1,5) ]

def variants(s, e, a):
    return ss[len(a) - (s in a)]

a = [int(line) for line in open("input.txt")]
a.sort()

b = [[j-i for i, j in zip([0] + a, a + [max(a)+3])].count(c) for c in (1,3)]

var, sa, sv, j = 1, 0, 0, 0
for i in range(len(a)):
    if a[i] - j == 3:
        var = var * variants(sv,j,a[sa:i-1])
        sa, sv = i, a[i]
    j = a[i]

if sv != j:
    var = var * variants(sv,j,a[sa:-1])

print("Part1: %d\nPart2: %d" % (b[0] * b[1], var))
