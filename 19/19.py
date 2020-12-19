
import re
from enum import Enum

class K(Enum):
    stop = 1
    single = 2
    multi = 3

def create_rule(txt):
	m = re.match(r"^\s*\"([ab])\"$", txt)
	if m:
		return (K.stop, m.group(1))
	tl = [[ int(v) for v in re.findall(r"(\b\d+\b)", part)] for part in txt.split('|')]
	if len(tl) ==1:
		return (K.single, tl[0])
	else:
		return (K.multi, tl[0], tl[1])

def check(rules, txt, part):

	def eat_wl(i, wl):
		if not len(wl):
			return len(txt) == i
		return eat(wl[0], i, wl[1:])

	def eat(rn, i, wl):
		r = rules[rn]
		if r[0] == K.stop:
			if i < len(txt) and txt[i] == r[1]:
				return eat_wl(i+1, wl)
			else:
				return False
		elif r[0] == K.single:
			ok = eat_wl(i, r[1] + wl)
			if not ok and part == 2:
				if rn == 8:
					ok = eat_wl(i, [42, 8] + wl)
				elif rn == 11:
					ok = eat_wl(i, [42, 11, 31] + wl)
			return ok
		else:
			ok = eat_wl(i, r[1] + wl)
			if ok:
				return ok
			return eat_wl(i, r[2] + wl)

	return eat(0, 0, [])

ichunks = [[line for line in chunk.strip().split('\n') if line[0] != '#']
           for chunk in open("input.txt").read().split('\n\n')]

rules = {}
for rl in ichunks[0]:
	rn, rp2 = rl.split(":")
	rules[int(rn)] = create_rule(rp2)

sum1,sum2 = 0, 0
for msg in ichunks[1]:
	sum1 += check(rules, msg, 1)
	sum2 += check(rules, msg, 2)

print("Part1: %d\nPart2: %d" % (sum1, sum2))
