earliest, buses = open("/Users/ciaran.whyte/dev/aoc2020/day13/input.txt").read().splitlines()

# earliest, buses = """939
# 7,13,x,x,59,x,31,19
# """.splitlines()

buses = [int(x) for x in buses.split(',') if x != 'x']
earliest = int(earliest)

current=earliest
while True:
    current+=1
    departing_bus=[b for b in buses if current%b==0]
    if departing_bus:
        print(departing_bus[0])
        print(f"PART 1: {(current-earliest)*departing_bus[0]}")
        break