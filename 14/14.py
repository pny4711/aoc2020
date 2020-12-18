
def part1(data):
    mem = {}
    om, am = 0, 0xFFFFFFFFF
    for k, vb in data:
        if k == 'mask':
            om = sum([ 1 << i for i, v in enumerate(vb[::-1]) if v == '1'])
            am = sum([ 1 << i for i, v in enumerate(vb[::-1]) if v == '1' or v == 'X'])
        else:
            adr_parts = k.split('[')
            adr = int(adr_parts[1][:-1])
            mem[adr] = (int(vb) & am) | om

    return sum(mem.values())


def part2(data):
    mem = {}
    xmasks = [(0,0xFFFFFFFFF)]
    for k, vb in data:
        if k == 'mask':
            om = sum([ 1 << i for i, v in enumerate(vb[::-1]) if v == '1'])
            xm = [i for i, v in enumerate(vb[::-1]) if v == 'X']
            xmasks = [(om, 0xFFFFFFFFF)]
            for xi in xm:
                t = [(om | x << xi, am & ~(((x+1) & 1) << xi))
                     for om,am in xmasks for x,y in ((0,1),(1,0))]
                xmasks = t
        else:
            adr_parts = k.split('[')
            adr = int(adr_parts[1][:-1])
            for xom, xam in xmasks:
                mem[(adr & xam) | xom] = int(vb)
    return sum(mem.values())

a = [line.strip().split(' = ') for line in open("input.txt")]

print("Part1: %d" % part1(a))
print("Part2: %d" % part2(a))
