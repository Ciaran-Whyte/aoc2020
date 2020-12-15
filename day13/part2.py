# earliest, buses = open("/Users/ciaran.whyte/dev/aoc2020/day13/input.txt").read().splitlines()

earliest, buses = """939
17,x,13,19
""".splitlines()

buses = [(int(x),idx) for idx, x in enumerate(buses.split(',')) if x != 'x']
print(buses)
x = max([x[0] for x in buses])
print(x)
earliest = 0

current=earliest
while True:
    current+=x
    departing_bus=[]

    for b in buses: 
        if (current+b[1])%b[0]==0:
            departing_bus.append(b[0])
        else:
            break

    if len(departing_bus) == len(buses):
        print(departing_bus)
        print(f"PART 2: {current}")
        exit(0)
    
    print(current)