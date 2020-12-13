import copy
input_lines = list(map(list,open("/Users/ciaran.whyte/dev/aoc2020/day11/input.txt").read().splitlines()))

# input_lines = list(map(list, """L.LL.LL.LL
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

# input_lines = list(map(list, """#.##.##.##
# #######.##
# #.#.#..#..
# ####.##.##
# #.##.##.##
# #.#####.##
# ..#.#.....
# ##########
# #.######.#
# #.#####.##
# """.splitlines()))


def pprint(floor_plan):
    for y in floor_plan:
        print("".join(y))


pprint(input_lines)


def get_num_of_adjacent(x: int, y: int, floor_plan: list) -> int:
    total_occ = 0

    # debug =  x == 0 and y == 1
    debug =  False

    if debug:
        print(f"--------------------")
        print(f"{x},{y}")

    if floor_plan[y][x] == '.':
        return -1

    for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        new_y = y+dy
        new_x = x+dx

        while True:

            if debug:
                print(f"heading ({dy},{dx}) @  ({new_y},{new_x})")

            if new_y < 0 or new_y >= len(floor_plan):
                if debug:
                    print(f"hit OOB")
                break
            if new_x < 0 or new_x >= len(floor_plan[0]):
                if debug:
                    print(f"hit OOB")
                break

            if debug:
                print(f"FOUND {floor_plan[new_y][new_x]}")

            if floor_plan[new_y][new_x] == 'L':
                if debug:
                    print(f"hit L")
                break
            elif floor_plan[new_y][new_x] == '#':
                if debug:
                    print(f"hit #")
                total_occ += 1
                break

            if debug:
                print(f"hit .")
            
            new_y += dy
            new_x += dx
        
        if debug:
            print(f"----------{total_occ}----------")

    return total_occ


current_plan = copy.deepcopy(input_lines)
updated_plan = copy.deepcopy(input_lines)
while True:
    changes_made = 0
    for y in range(len(current_plan)):
        for x in range(len(input_lines[0])):
            adjacent_seats = get_num_of_adjacent(x, y, current_plan)
            if adjacent_seats == 0 and updated_plan[y][x] != '#':
                updated_plan[y][x] = '#'
                changes_made += 1
            elif adjacent_seats >= 5 and updated_plan[y][x] != 'L':
                updated_plan[y][x] = 'L'
                changes_made += 1

    current_plan = copy.deepcopy(updated_plan)
    print("##################################################")
    pprint(current_plan)

    if changes_made == 0:
        print(f"Part 2: {sum([row.count('#') for row in current_plan])}")
        exit(0)
    # exit(0)
