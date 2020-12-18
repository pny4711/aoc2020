
def boundaries(cube):
    xs = [x for x,_,_,_ in list(cube)]
    ys = [y for _,y,_,_ in list(cube)]
    zs = [z for _,_,z,_ in list(cube)]
    ws = [w for _,_,_,w in list(cube)]

    return (min(xs), max(xs)+1, min(ys), max(ys)+1, min(zs), max(zs)+1, min(ws), max(ws)+1)


def active(cube, x, y, z, w):
    an = len([(x+a,y+b,z+c,w+d) for a in (-1,0,1) for b in (-1,0,1) for c in (-1,0,1)
	      for d in (-1,0,1) if (a,b,c,d) != (0,0,0,0) and (x+a,y+b,z+c,w+d) in cube])
    if (x,y,z,w) in cube:
        return an == 2 or an == 3
    else:
        return an == 3


def step(cube, xl, xh, yl, yh, zl, zh, wl, wh):
    cube1 = set()
    ws = set()
    for x,y,z,w in list(cube):
        nb = [(xx,yy,zz,ww) for xx in range(x-1, x+2) for yy in range(y-1, y+2)
	      for zz in range(z-1, z+2) for ww in range(w-1,w+2)
	      if (xx,yy,zz,ww) not in ws]
        ws.update(set(nb))

    for cx,cy,cz,cw in list(ws):
        if active(cube, cx, cy, cz, cw):
            cube1.add((cx,cy,cz,cw))
    return cube1


def print_cube(c, xl, xh, yl, yh, zl, zh, wl, wh):
    for w in range(wl, wh):
        for z in range(zl, zh):
            print("Z = %d, W = %d" % (z, w))
            for y in range(yl, yh):
                l = ""
                for x in range(xl, xh):
                    if (x,y,z,w) in c:
                        l += "#"
                    else:
                        l += "."
                print(l)
            print("")

a = [line.strip() for line in open("input.txt")]

cube = set()

minx, miny, minz, minw = 0, 0, 0, 0
maxx = len(a[0])
maxy = len(a)
maxz, maxw = 1, 1

for y,l in enumerate(a):
    for x,s in enumerate(l):
        if s == '#':
            cube.add((x,y,0,0))

# print("---------------------------------")
# print_cube(cube, minx, maxx, miny, maxy, minz, maxz, minw, maxw)

for boot in range(1,7):
    print("Step %d" % boot)

    cube = step(cube, minx, maxx, miny, maxy, minz, maxz, minw, maxw)
#    print("checking new boundaries")
    minx, maxx,miny, maxy, minz, maxz, minw, maxw = boundaries(cube)

#	print_cube(cube, minx, maxx, miny, maxy, minz, maxz, minw,maxw)

print(len(cube))
