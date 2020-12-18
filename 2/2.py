
import re

ok1 = 0
ok2 = 0

for line in open("input.txt"):
	(slow, shigh, match, pwd) = re.split('-| |: ', line.strip())
	low = int(slow)
	high = int(shigh)

	ok1 += (low <= pwd.count(match[0]) <= high)
	ok2 += ((pwd[low-1] in match) ^ (pwd[high-1] in match))

print("%d ok1 passwords" % ok1)
print("%d ok2 passwords" % ok2)

print(len([p for p in [[p for p in re.split('-| |: ', line.strip())] for line in open("input.txt")]
		if int(p[0]) <= p[3].count(p[2]) <= int(p[1])]))

print(len([p for p in [[p for p in re.split('-| |: ', line.strip())] for line in open("input.txt")]
		if (p[3][int(p[0])-1] in p[2]) ^ (p[3][int(p[1])-1] in p[2])]))
