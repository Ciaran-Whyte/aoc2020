import copy
input_lines = list(map(list,open("/Users/ciaran.whyte/dev/aoc2020/day11/input.txt").read().splitlines()))

# input_lines = list(map(list,"""L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL
# """.splitlines()))

def pprint(floor_plan):
    for y in floor_plan:
        print(y)

pprint(input_lines)

def get_num_of_adjacent(x: int, y: int, floor_plan: list)-> int: 
    total_occ=0

    if floor_plan[y][x] == '.':
        return -1

    for dy, dx in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
        if y+dy < 0 or y+dy >= len(floor_plan):
            continue
        if x+dx < 0 or x+dx >= len(floor_plan[0]):
            continue

        if floor_plan[y+dy][x+dx] == '#':
            total_occ+=1

    return total_occ


current_plan = copy.deepcopy(input_lines)
updated_plan = copy.deepcopy(input_lines)
while True:
    changes_made=0
    for y in range(len(current_plan)):
        for x in range(len(input_lines[0])):
            adjacent_seats = get_num_of_adjacent(x, y, current_plan)
            if adjacent_seats == 0 and updated_plan[y][x] !='#':
                updated_plan[y][x]='#'
                changes_made+=1
            elif adjacent_seats >= 4 and updated_plan[y][x] !='L':
                updated_plan[y][x]='L'
                changes_made+=1

    current_plan = copy.deepcopy(updated_plan)
    print("##################################################")      
    pprint(current_plan)

    if changes_made == 0:
        print(f"Part 1: {sum([row.count('#') for row in current_plan])}")
        exit(0)