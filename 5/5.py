ids = [ sum([(1<<p) * (line.strip()[9-p] in 'BR') for p in range(10)]) for line in open("input.txt")]

print("1, %d highest id" % max(ids))
print("2, %d my id" % max([ s if not s in ids else 0 for s in range(min(ids), max(ids))]))
