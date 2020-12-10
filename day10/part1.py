import itertools
import networkx

# input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day10/input.txt").read().splitlines()

input_lines = """16
10
15
5
1
11
7
19
6
12
4
""".splitlines()
 
adapters = sorted(list(map(int, input_lines)))

built_in_joltage_adapter = max(adapters) + 3
adapters.append(built_in_joltage_adapter)

one_jolt_diff=0
three_jolt_diff=0

print(adapters)

previous_adapter=0

for adapter in adapters:
    print(f"Chain:{previous_adapter} A:{adapter} Diff:{adapter-previous_adapter}")

    if adapter-previous_adapter == 1:
        one_jolt_diff+=1
    elif adapter-previous_adapter == 3:
        three_jolt_diff+=1
    previous_adapter=adapter

print(f"d1:{one_jolt_diff}, d3:{three_jolt_diff} = PART1: {one_jolt_diff * three_jolt_diff}")