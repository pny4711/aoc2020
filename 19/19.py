
import re
from enum import Enum

def tl2str(tl):
    return " ".join(tl)

def txtpart(txt,i):
	return "%s%s (%d)" % ("                                       "[:i], txt[i:], i)


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

	def eat_wl(i, wl, n):
		if not len(wl):
			return len(txt) == i
		return eat(wl[0], i, wl[1:], n + 1)


	def p(n, mode, rn, i, msg, wl):
#		print("%-2s: %3d %-30s | %s\n\t\t%s" % (mode, rn, msg, str(wl), txtpart(txt,i)))

#		if mode in ('S','M1','M2','M8','M11'):
#			print("[%d] %s + %s" % (rn, msg, str(wl)))


#		si = max(0, i - 5)
#		if i < len(txt):
#			ei = min(i + 6, len(txt))
#			ix = min(i + 1, len(txt))
#			dots = "..." if ei < len(txt) else "   "
#			print("%s %d:%-2s, %s, [%d] %s %s %-5s%s |  %s" %
#				  ("".ljust(2*n),rn, mode, msg, i, txt[si:i], txt[i], txt[ix:ei],dots, str(wl)))
#		else:
#			print("%s %d:%-2s, %s, [%d] %s {end} |  %s" %
#				  ("".ljust(2*n),rn, mode, msg, i, txt[si:i], str(wl)))
		pass

	def eat(rn, i, wl, n):
		r = rules[rn]
		if r[0] == K.stop:
			if i < len(txt) and txt[i] == r[1]:
				p(n, "+", rn, i, "ok '%s'" % (r[1]), wl)
				return eat_wl(i+1, wl, n)
			else:
				p(n, "X", rn, i, "fail '%s'" % (r[1]), wl)
				return False

		elif r[0] == K.single:
			p(n, "S", rn, i, str(r[1]), wl)
			wl1 = r[1] + wl
			ok = eat_wl(i, wl1, n)
			if not ok and part == 2:
				if rn == 8:
					wl2 = [42, 8] + wl
					p(n, "M8", rn, i, "[42, 8]", wl)
					ok = eat_wl(i, wl2, n)
				elif rn == 11:
					p(n, "M11", rn, i, "[42, 11, 31]", wl)
					wl2 = [42, 11, 31] + wl
					ok = eat_wl(i, wl2, n)
			return ok
		else:
			p(n, "M1", rn, i, str(r[1]), wl)
			wl1 = r[1] + wl
			ok = eat_wl(i, wl1, n)
			if ok:
				return ok
			p(n, "M2", rn, i, str(r[2]), wl)
			wl2 = r[2] + wl
			return eat_wl(i, wl2, n)

	return eat(0, 0, [], 0)

ichunks = [[line for line in chunk.strip().split('\n') if line[0] != '#']
           for chunk in open("input.txt").read().split('\n\n')]

rules = {}

for rl in ichunks[0]:
	rn, rp2 = rl.split(":")
	rules[int(rn)] = create_rule(rp2)

sum1 = 0
sum2 = 0
for msg in ichunks[1]:
	if check(rules, msg, 1):
		sum1 += 1

	if check(rules, msg, 2):
		sum2 += 1

print("Part1: %d\nPart2: %d" % (sum1, sum2))








