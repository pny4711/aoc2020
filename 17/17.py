
def boundaries(cube):
    xs = [x for x,_,_ in list(cube)]
    ys = [y for _,y,_ in list(cube)]
    zs = [z for _,_,z in list(cube)]

    return (min(xs), max(xs)+1, min(ys), max(ys)+1, min(zs), max(zs)+1)


def active(cube, x, y, z):
    an = len([(x+a,y+b,z+c) for a in (-1,0,1) for b in (-1,0,1) for c in (-1,0,1)
              if (a,b,c) != (0,0,0) and (x+a,y+b,z+c) in cube])
    if (x,y,z) in cube:
        return an == 2 or an == 3
    else:
        return an == 3

def step(cube, xl, xh, yl, yh, zl, zh):
    cube1 = set()
    ws = set()
    for x,y,z in list(cube):
        nb = [(xx,yy,zz) for xx in range(x-1, x+2) for yy in range(y-1, y+2)
              for zz in range(z-1, z+2) if (xx,yy,zz) not in ws]
        ws.update(set(nb))

    for cx,cy,cz in list(ws):
        if active(cube, cx, cy, cz):
            cube1.add((cx,cy,cz))
    return cube1


def print_cube(c, xl, xh, yl, yh, zl, zh):
    for z in range(zl, zh):
        print("Z = %d" % z)
        for y in range(yl, yh):
            l = ""
            for x in range(xl, xh):
                if (x,y,z) in c:
                    l += "#"
                else:
                    l += "."
                    print(l)
        print("")

a = [line.strip() for line in open("input.txt")]

cube = set()

minx, miny, minz = 0, 0, 0
maxx = len(a[0])
maxy = len(a)
maxz = 1

for y,l in enumerate(a):
    for x,s in enumerate(l):
        if s == '#':
            cube.add((x,y,0))

# print_cube(cube, minx, maxx, miny, maxy, minz, maxz)

for boot in range(1,7):
    print("Step %d" % boot)

    cube = step(cube, minx, maxx, miny, maxy, minz, maxz)
    minx, maxx,miny, maxy, minz, maxz = boundaries(cube)

    # print_cube(cube, minx, maxx, miny, maxy, minz, maxz)

print(len(cube))
