def readInputs(file_name: str) -> list[str]:
    with open(file_name) as f:
        lineInput = f.readlines()
    return [x for x in lineInput]


# lines = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
lines = readInputs("/Users/ciaran.whyte/dev/aoc2020/day2/input.txt")

def is_password_valid(pos_one: int, pos_two: int, character: str, password: str) -> bool:
    return (password[pos_one-1] == character) != (password[pos_two-1] == character)


valid_count=0
for line in lines:
    min_max , char, password = line.split()
    min_count, max_count = [int(p) for p in min_max.split('-')]
    if is_password_valid(min_count, max_count, char.replace(":",""), password):
        valid_count+=1

print(f"valid_count {valid_count}")