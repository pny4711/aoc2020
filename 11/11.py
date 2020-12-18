def occupied_adjacent(l, c, a):
    ll, lh = max(0, l-1), min(len(a), l+2)
    cl, ch = max(0, c-1), min(len(a[0]), c+2)

    s = sum([len([f for f in aa[cl:ch] if f == '#']) for aa in a[ll:lh]])
    s -= a[l][c] == '#'
    return s

def occupied_direction(l, c, a, ol, oc):
    if ol == 0 and oc == 0:
        return 0
    lt = l + ol
    ct = c + oc
    while 0 <= lt < len(a) and 0 <= ct < len(a[0]):
        if a[lt][ct] in ['#', 'L']:
            return a[lt][ct] == '#'
        lt += ol
        ct += oc
    return 0

def occupied_directions(l, c, a):
    return sum([ sum([occupied_direction(l, c, a, ol, oc) for oc in range(-1,2)])
                 for ol in range(-1,2)])

rules = [{ '.' : lambda l, c, a : a[l][c],
           'L' : lambda l, c, a : '#' if occupied_adjacent(l, c, a) == 0 else 'L',
           '#' : lambda l, c, a : '#' if occupied_adjacent(l, c, a) < 4 else 'L'
          },

	 { '.' : lambda l, c, a : a[l][c],
           'L' : lambda l, c, a : '#' if occupied_directions(l, c, a) == 0 else 'L',
           '#' : lambda l, c, a : '#' if occupied_directions(l, c, a) < 5 else 'L'
          }]

#def next_step(a,part):
#	b = []
#	for l in range(len(a)):
#		bl = ""
#		for c in range(len(a[l])):
#			bl += rules[part][a[l][c]](l, c, a)
#		b.append(bl)
#	return b

def next_step(a,part):
    return [ "".join([rules[part][a[l][c]](l, c, a) for c in range(len(a[l]))])
        for l in range(len(a))]

def run(a, part):
    b = next_step(a,part)
    while b != a:
        a = b
        b = next_step(a,part)
    return b

a = [line.strip() for line in open("input.txt")]
res = [sum([bl.count('#')  for bl in run(a, part)]) for part in [0,1]]

print("Part1: %d\nPart2: %d" % (res[0], res[1]))
