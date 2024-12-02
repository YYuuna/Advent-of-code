'''Part 1
    Count the number of valid passports - those that have all required fields.
    Treat cid as optional. In your batch file, how many passports are valid?'''

import re

input = open("day-4-input.txt", "r")
passports = []
valid_passports = []
valid = True
valid_passports_count = 0
input = input.read().split("\n\n")

for passport in input:
    passport = re.split('[ :\n]', passport)
    it = iter(passport)
    passport = dict(zip(it, it))
    print(passport)
    if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport.keys()):
        if not (len(passport["byr"]) == 4 and 2002 >= int(passport["byr"]) >= 1920):
            continue
        if not (len(passport["iyr"]) == 4 and 2010 <= int(passport["iyr"]) <= 2020):
            continue
        if not (len(passport["eyr"]) == 4 and 2020 <= int(passport["eyr"]) <= 2030):
            continue
        if not (("cm" in passport["hgt"] and 193>=int(passport["hgt"].split("cm")[0])>=150)
                or ("in" in passport["hgt"] and 76>=int(passport["hgt"].split("in")[0])>=59)):
            continue

        if passport["hcl"][0] == "#" and len(passport["hcl"].split("#")[1])==6:
            valid_hcl=True
            for c in passport["hcl"].split("#")[1]:
                if not(('a' <= c <= 'f') or ('9' >= c >= '0')):
                    valid_hcl=False
                    break
            if not valid_hcl:continue
        else:
            continue
        if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            continue
        if len(passport['pid']) == 9:
            valid_pid = True
            for d in passport['pid']:
                if not d.isdecimal():
                    valid_pid = False
                    break
            if not valid_pid: continue
        else:
            continue
        valid_passports_count += 1

print(valid_passports_count)
