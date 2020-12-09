import itertools

input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day9/input.txt").read().splitlines()
preamble=25

# preamble=5
# input_lines = """35
# 20
# 15
# 25
# 47
# 40
# 62
# 55
# 65
# 95
# 102
# 117
# 150
# 182
# 127
# 219
# 299
# 277
# 309
# 576
# """.splitlines()
 
input_lines = list(map(int, input_lines))

target=None
def num_is_invalid(num, preamble_list):
    for x in itertools.combinations(preamble_list, 2):
        if sum(x) == num:
            print(f"{x[0]} + {x[1]} == {num}   VALID" )
            return False
    return True

for idx, num in enumerate(input_lines[preamble:]):
    if num_is_invalid(num, input_lines[idx:preamble+idx]):
        target=num
        print(f"PART1: {target}")
        break
            
sliding_window_size=2
while True:
    for idx in range(len(input_lines)-sliding_window_size):
        if sum(input_lines[idx:idx+sliding_window_size]) == target:
            contiguous_set=input_lines[idx:idx+sliding_window_size]
            print(contiguous_set)
            print(f"PART2: {min(contiguous_set) + max(contiguous_set)}")
            exit(0)
    sliding_window_size+=1
    print(f"increasing the sliding window size to {sliding_window_size}")

