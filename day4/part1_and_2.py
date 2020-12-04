
import re

input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day4/input.txt").read()
# input_lines = """
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f

# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022

# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
# """

REQUIRED_KEYS=["byr","iyr","eyr","hgt","hcl","ecl","pid"]
OPTIONAL="cid"

def is_valid(passport: str)-> bool:
    print(passport)
    dict_passport = { x.split(':')[0]: x.split(':')[1] for x in re.findall('\w+:\S+', passport)}
    print(dict_passport)
    for key in REQUIRED_KEYS:
        if key not in dict_passport.keys():
            print(f"Missing {key}: invalid")
            return False

    if not (1920 <= int(dict_passport["byr"]) <= 2002):
        print(f"Invalid BYR {dict_passport['byr']}")
        return False
    
    if not (2010 <= int(dict_passport["iyr"]) <= 2020):
        print(f"Invalid iyr {dict_passport['iyr']}")
        return False
    
    if not (2020 <= int(dict_passport["eyr"]) <= 2030):
        print(f"Invalid eyr {dict_passport['eyr']}")
        return False
    
    if "cm" in dict_passport["hgt"] and not (150 <= int(dict_passport["hgt"].replace("cm","")) <= 193):
        print(f"Invalid hgt cms {dict_passport['hgt']}")
        return False 
    elif "in" in dict_passport["hgt"] and not (59 <= int(dict_passport["hgt"].replace("in","")) <= 76):
        print(f"Invalid hgt inches {dict_passport['hgt']}")
        return False 
    elif "cm" not in  dict_passport["hgt"] and "in" not in dict_passport["hgt"]:
        print(f"Invalid hgt formate {dict_passport['hgt']}")
        return False 

    if len(re.findall('^#[0-9a-f]{6}$', dict_passport["hcl"])) == 0:
        print(f"Invalid hcl {dict_passport['hcl']}")
        return False 

    if dict_passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print(f"Invalid ecl {dict_passport['ecl']}")
        return False 

    if len(re.findall('^[0-9]{9}$', dict_passport["pid"])) == 0:
        print(f"Invalid pid {dict_passport['pid']}")
        return False 
    
    print("# VALID #")
    return True

valid_count=0
for passport in input_lines.split("\n\n"):
    if is_valid(passport):
        valid_count+=1
    print("\n\n")

print(f"valid_count: {valid_count}")


