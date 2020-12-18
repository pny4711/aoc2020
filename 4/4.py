import re

rules = { "byr": lambda v : 1920 <= int(v) <= 2002,
          "iyr": lambda v : 2010 <= int(v) <= 2020,
	  "eyr": lambda v : 2020 <= int(v) <= 2030,
	  "hgt": lambda v : ((v[-2:] == 'cm' and 150 <= int(v[:-2]) <= 193) or
	       		     (v[-2:] == 'in' and 59 <= int(v[:-2]) <= 76)),
	  "hcl": lambda v : re.match("#[0-9a-fA-F]{6}", v ),
	  "ecl": lambda v : v in ['amb','blu','brn','gry','grn','hzl','oth'],
	  "pid": lambda v : re.match(r"^\d{9}$", v)
	 }

def valid1(pd):
    return all([k in pd for k in rules])

def valid2(pd):
    return all([rules[k](pd[k]) for k in rules])

valid_passports1 = 0
valid_passports2 = 0

for line in open("input.txt").read().split('\n\n'):
    passport_data = {}
    for pdl in line.replace('\n', ' ').split():
        key, data = pdl.split(':')
        passport_data[key] = data

    if valid1(passport_data):
        valid_passports1 += 1
        if valid2(passport_data):
            valid_passports2 += 1

print("1, %d valid passports" % valid_passports1)
print("2, %d valid passports" % valid_passports2)
