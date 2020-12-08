input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day8/input.txt").read().splitlines()
# input_lines = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6
# """.splitlines()
 
acc=0
current_instruction_pointer=0

while input_lines[current_instruction_pointer] != 'brk':
    instruction, argument = input_lines[current_instruction_pointer].split()
    input_lines[current_instruction_pointer]='brk'

    if instruction == 'nop':
        current_instruction_pointer+=1
    elif instruction == 'jmp':
        current_instruction_pointer+=int(argument)
    else:
        current_instruction_pointer+=1
        acc+=int(argument)

print(f"PART1: {acc}")
