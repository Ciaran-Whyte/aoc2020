def solve(input_list: list, total_turns: int) -> int:
    d = { num:index for index, num in enumerate(input_list, 1) } 
    current = input_list[-1]
    turn   = len(input_list)

    while True:
        previous   = d.get(current)
        d[current] = turn
        current    = turn-previous if previous else 0   
        turn+=1

        if turn == total_turns:
            return current

input_list = [2,0,1,9,5,19]
print(f"Part 1 answer: {solve(input_list, 2020)}")
print(f"Part 2 answer: {solve(input_list, 30000000)}")