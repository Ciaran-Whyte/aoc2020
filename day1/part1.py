def readInputs(file_name: str) -> list[int]:
    with open(file_name) as f:
        lineInput = f.readlines()
    return [int(x) for x in lineInput]

# numbers=[1721, 979, 366, 299, 675, 1456]

def do_we_have_a_twenty_twenty_pair(input_one: int, remaining_numbers: list[int]) -> (bool, int):
    for x in remaining_numbers:
        if x + input_one == 2020:
            return True, x
    return False, None


numbers=readInputs("/Users/ciaran.whyte/dev/aoc2020/day1/input.txt")

for idx, num in enumerate(numbers):
    match, paired_num = do_we_have_a_twenty_twenty_pair(num, numbers[idx:])
    if match:
        print(f"{num} + {paired_num} == 2020")
        print(f"{num} * {paired_num} == {num * paired_num}")

