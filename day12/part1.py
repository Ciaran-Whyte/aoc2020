input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day12/input.txt").read().splitlines()

# input_lines = """F10
# N3
# F7
# R90
# F11
# """.splitlines()

d_keys=["N","E","S","W"]

amounts = {
    "N": 0,
    "E": 0,
    "S": 0,
    "W": 0
}
facing = 90

for direction in input_lines:
    command=direction[0]
    command_value=int(direction[1:])

    if command == "F":
        foward=d_keys[(facing%360)//90]
        amounts[foward]= amounts[foward] + command_value
    elif command in d_keys:
        amounts[command] =  amounts[command] + command_value
    elif command == "L":
        facing-=command_value
    elif command == "R":
        facing+=command_value

print(abs(amounts["N"]-amounts["S"]) + abs(amounts["W"]-amounts["E"]))