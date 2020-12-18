i = { "nop":  lambda p, pc, acc : (pc+1,acc),
      "acc":  lambda p, pc, acc : (pc+1,acc+p),
      "jmp":  lambda p, pc, acc : (pc+p,acc)
     }

def run(m, xseen = []):
    pc, acc = 0,0
    seen = set(xseen)
    while pc not in seen:
        seen.add(pc)
        (pc, acc) = i[m[pc][0]](int(m[pc][1]), pc, acc)
    return (pc, acc)

def run2(m):
    xx = { 'jmp' : 'nop', 'nop' : 'jmp' }
    for l in range(len(m)):
        if m[l][0] in xx:
            m[l][0] = xx[m[l][0]]
            (x, a) = run(m,[len(m)])
            m[l][0] = xx[m[l][0]]
            if x == len(m):
                return (x, a)

mem = [line.split() for line in open("input.txt")]

print("Part 1: %d\nPart 2: %d" % (run(mem)[1], run2(mem)[1]))
