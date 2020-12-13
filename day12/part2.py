input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day12/input.txt").read().splitlines()

# input_lines = """F10
# N3
# F7
# R90
# F11
# """.splitlines()



#       N
#   W       E
#       S
          #W-E #N-S    
waypoint = [10, 1]
location = [0, 0]

for direction in input_lines:
    command = direction[0]
    command_value = int(direction[1:])

    if command == "F":
        location[0] = location[0] + waypoint[0] * command_value
        location[1] = location[1] + waypoint[1] * command_value
    elif command == "N":
        waypoint[1] = waypoint[1] + command_value
    elif command == "S":
        waypoint[1] = waypoint[1] - command_value
    elif command == "E":
        waypoint[0] = waypoint[0] + command_value
    elif command == "W":
        waypoint[0] = waypoint[0] - command_value
    elif command == "L":
        for l in range(command_value//90):
            x, y = waypoint
            waypoint=[-y, x]
    elif command == "R":
        for r in range(command_value//90):
            x, y = waypoint
            waypoint=[y, -x]

print(abs(location[0]) + abs(location[1]))
