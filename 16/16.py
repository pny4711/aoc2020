import re
from functools import reduce

ichunks = [[line for line in chunk.strip().split('\n')]
           for chunk in open("input.txt").read().split('\n\n')]

rules = []
ok_set = set()
for r in ichunks[0]:
    m = re.match(r"([^:]+):\s(\d+)-(\d+)\sor\s(\d+)-(\d+)", r)
    s1 = set([v for v in range(int(m.group(2)), int(m.group(3))+1)])
    rules.append((m.group(1), s1.union(set([v for v in range(int(m.group(4)), int(m.group(5))+1)]))))
    ok_set.update(rules[-1][1])

my_ticket = [int(v) for v in ichunks[1][1].strip().split(',')]
ok_nt = [ [int(v) for v in line.split(',')] for line in ichunks[2][1:]
	  if not sum([int(v) for v in line.split(',') if int(v) not in ok_set])]

all_num = [ set([v[id] for v in ok_nt]) for id in range(len(rules))]
ok_rules = [ set([ j for j,r in enumerate(rules) if r[1].issuperset(all_num[i])])
             for i in range(len(rules))]

again = True
singles = []
rules_map = {}
while again:
    again = False
    for i,r in enumerate(ok_rules):
        if i not in singles and len(r) == 1:
            z = list(r)[0]
            singles.append(i)
            rules_map[i] = rules[z]
            again = True
            for j,u in enumerate(ok_rules):
                if i != j:
                    ok_rules[j].discard(z)

sum1 = sum([ sum([int(v) for v in line.split(',') if int(v) not in ok_set])
             for line in ichunks[2][1:]])
prod2 = reduce(lambda x, y: x * y, [ v for i, v in enumerate(my_ticket)
                                     if rules_map[i][0].find("departure") != -1])

# for i, v in enumerate(my_ticket):
#    print("%-20s: %d" % (rules_map[i][0], v))

print(sum1)
print(prod2)
