
f  = {  90 : "E", 180 : "S", 270 : "W", 0 : "N" }

r = { "E": lambda v, s : (s[0], s[1], s[2] - v),
      "S": lambda v, s : (s[0], s[1] - v, s[2]),
      "W": lambda v, s : (s[0], s[1], s[2] + v),
      "N": lambda v, s : (s[0], s[1] + v, s[2]),
      "R": lambda v, s : ((s[0] + v) % 360, s[1], s[2]),
      "L": lambda v, s : ((s[0] - v) % 360, s[1], s[2]),
      "F": lambda v, s : r[f[s[0]]](v, s)
     }

ror = {  0  : lambda wp : wp,
    	90  : lambda wp : (wp[1], -wp[0]),
	180 : lambda wp : (-wp[0], -wp[1]),
       	270 : lambda wp : (-wp[1], wp[0])
       }

r2 = { "E": lambda v, p, wp : (p, (wp[0], wp[1] - v)),
       "S": lambda v, p, wp : (p, (wp[0] - v, wp[1])),
       "W": lambda v, p, wp : (p, (wp[0], wp[1] + v)),
       "N": lambda v, p, wp : (p, (wp[0] + v, wp[1])),
       "R": lambda v, p, wp : (p, ror[v](wp)),
       "L": lambda v, p, wp : (p, ror[360 - v](wp)),
       "F": lambda v, p, wp : ((p[0] + v * wp[0], p[1] + v * wp[1]), wp),
      }

a = [(line[0], int(line[1:])) for line in open("input.txt")]

p = (90, 0, 0)
p2 = (0, 0)
wp = (1, -10)
for m in a:
    p = r[m[0]](m[1], p)
    p2, wp = r2[m[0]](m[1], p2, wp)

print("Part1: %d\nPart2: %d" % (abs(p[1]) + abs(p[2]), abs(p2[0]) + abs(p2[1])))
