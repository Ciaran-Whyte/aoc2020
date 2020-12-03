def readInputs(file_name: str) -> list[str]:
    with open(file_name) as f:
        return f.read().splitlines()

map = readInputs("/Users/ciaran.whyte/dev/aoc2020/day3/input.txt")

# map = [
#     "..##.......",
#     "#...#...#..",
#     ".#....#..#.",
#     "..#.#...#.#",
#     ".#...##..#.",
#     "..#.##.....",
#     ".#.#.#....#",
#     ".#........#",
#     "#.##...#...",
#     "#...##....#",
#     ".#..#...#.#",
# ]

def get_slope(right: int, down: int, map: list[str]) -> int:
    tree_count, x, y = 0, 0, 0

    while y < len(map):
        x = (x+right) % len(map[0])
        y = y+down

        if y >= len(map):
            print(f"Tree Count: {tree_count}")
            return tree_count

        if map[y][x] == '#':
            tree_count += 1


print(
    get_slope(1, 1, map)
    * get_slope(3, 1, map)
    * get_slope(5, 1, map)
    * get_slope(7, 1, map)
    * get_slope(1, 2, map)
)
