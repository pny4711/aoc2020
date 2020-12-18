import re

bags_db = {}
bdb2 = {}

for rule in [[re.findall(r"^(\w+\s\w+)\sbag", line), re.findall(r"(\d+)\s(\w+\s\w+)\sbag", line)]
             for line in open("input.txt")]:
    for inside in rule[1]:
        if inside[1] not in bags_db:
            bags_db[inside[1]] = set()
        bags_db[inside[1]].add(rule[0][0])
    bdb2[rule[0][0]] = rule[1]

def bags_containing(db, bag, seen_bags):
    if bag in db:
        for ii in db[bag]:
            if ii not in seen_bags:
                seen_bags.add(ii)
                bags_containing(db, ii, seen_bags)
    return len(seen_bags)

def bags_inside(db, bag, done_bags):
    if bag not in done_bags:
        done_bags[bag] = 1 + sum([int(nr) * bags_inside(db,c,done_bags)
                                          for (nr, c) in db[bag]])
    return done_bags[bag]

print("bags can contain shiny gold: %d" % bags_containing(bags_db, 'shiny gold', set()))
# Remove the outer most bag as it is not inside
print("bags inside shiny gold: %d" % (bags_inside(bdb2, 'shiny gold', {})-1))
