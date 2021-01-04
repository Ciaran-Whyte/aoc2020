input_lines= open("/Users/ciaran.whyte/dev/aoc2020/day14/input.txt").read().splitlines()

# input_lines = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0
# """.splitlines()


def apply_mask(mask, value):
    bin_value='{:036b}'.format(int(value))
    out=[]
    for idx, b in enumerate(mask):
        if b != 'X':
            out.append(b)
        else:
            out.append(bin_value[idx])

    return int("".join(out).lstrip("0"),2)

mask=None
mem={}

#'{:036b}'.format(11)
for line in input_lines:
    command, _, value = line.split()
    if command == "mask":
        mask=value
    else:
        mem[int(command[4:-1])] = apply_mask(mask, value)

print(f"PART1: {sum([mem[x] for x in mem.keys()])}")
