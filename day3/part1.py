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

right=3
down=1
tree_count=0

x=0
y=0

while y < len(map):
    x=(x+right)%len(map[0])
    y=y+down

    if y >= len(map):
        print(f"Tree Count: {tree_count}")
        break

    if map[y][x] == '#':
        tree_count+=1