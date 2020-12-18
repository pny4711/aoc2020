
import re

op = { '+' : lambda x,y : x+y,
       '*' : lambda x,y : x*y,
       None : lambda x,y : y
      }

def is_num(ch):
    return ch in '0123456789'

def fix_precidence(tl):
    otl = [t for t in tl]
    offs = 0

    def fix_bw(i):
        pl = 0
        i = i + offs - 1
        while 1:
            tt = otl[i]
            if pl == 0 and is_num(tt):
                otl.insert(i,'(')
                return 1
            elif tt == ")":
                pl += 1
            elif tt == "(":
                pl -= 1
                if pl == 0:
                    otl.insert(i,'(')
                    return 1
            i -= 1

    def fix_fw(i):
        pl = 0
        i = i + offs +1
        while 1:
            tt = otl[i]
            if pl == 0 and is_num(tt):
                otl.insert(i+1,')')
                return
            elif tt == "(":
                pl += 1
            elif tt == ")":
                pl -= 1
                if pl == 0:
                    otl.insert(i+1,')')
                    return
            i += 1

    for i,ch in enumerate(tl):
        while ch != otl[i+offs]:
            offs += 1
        if ch == "+":
            offs += fix_bw(i)
            fix_fw(i)
    return otl

def calc(tl):
    stack = []
    val = 0
    opc = None

    for t in tl:
        if is_num(t):
            val = op[opc](val, int(t))
            opc = None
        elif t in "+*":
            opc = t
        elif t == "(":
            stack.append((val, opc))
            opc = None
        elif t == ")":
            val0, opc0 = stack.pop()
            val = op[opc0](val0, val)
    return val

sum1 = 0
sum2 = 0
for line in open("input.txt"):

    tl = re.findall(r"([\d\(\)\+\*])", line.strip())
    tl2 = fix_precidence(tl)

    c = calc(tl)
    sum1 += c
    c2 = calc(tl2)
    sum2 += c2

print("\nPart1: %d\nPart2: %d" % (sum1,sum2))
