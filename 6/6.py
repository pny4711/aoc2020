
sum1=0
sum2=0
for group in open("input.txt").read().split('\n\n'):
    u = set([ys for p in group.split() for ys in p.strip()])
    sum1 += len(u)

    for ps in [{ys for ys in p.strip()} for p in group.split()]:
        u.intersection_update(ps)
    sum2 += len(u)


print("1, Sum of group yes: %d" % sum1)
print("2, Sum of all in group yes: %d" % sum2)
