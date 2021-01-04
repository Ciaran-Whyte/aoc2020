input_lines= open("/Users/ciaran.whyte/dev/aoc2020/day14/input.txt").read().splitlines()

# input_lines = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1
# """.splitlines()

def apply_memory_mappings(mask, memory_value, write_value):
    bin_value='{:036b}'.format(int(memory_value))
    out=[]
    for idx, b in enumerate(mask):
        if b == '0':
            out.append(bin_value[idx])
        elif b == '1':
            out.append('1')
        else:
            out.append('X')

    memory_mask = "".join(out)
    floating_numbers = memory_mask.count('X')

    for x in range(2**floating_numbers):
        bin_counter = list(str(bin(x)[2:].zfill(floating_numbers)))
        try:
            memory_address = int(memory_mask.replace('X','{}').format(*bin_counter).lstrip("0"),2)
        except ValueError:
            memory_address = 0
        print(f"writing: mem[{memory_address}]={write_value}")
        mem[memory_address]=int(write_value)
        

mask=None
mem={}
for line in input_lines:
    command, _, value = line.split()
    if command == "mask":
        mask=value
    else:
        memory_value=int(command[4:-1])
        apply_memory_mappings(mask, memory_value, value)

print(f"PART2: {sum([mem[x] for x in mem.keys()])}")
