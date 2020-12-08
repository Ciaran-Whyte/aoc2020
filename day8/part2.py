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
 

def run_boot_code(instructions: list[str]):
    acc=0
    current_instruction_pointer=0
    max_depth=current_instruction_pointer

    while instructions[current_instruction_pointer] != 'brk':
        instruction, argument = instructions[current_instruction_pointer].split()
        max_depth=max(max_depth,current_instruction_pointer)

        instructions[current_instruction_pointer]='brk'

        if instruction == 'nop':
            current_instruction_pointer+=1
        elif instruction == 'jmp':
            current_instruction_pointer+=int(argument)
        else:
            current_instruction_pointer+=1
            acc+=int(argument)

        if current_instruction_pointer >= len(instructions):
            return False, acc, max_depth
    
    return True, acc, max_depth

# Got to try all of the nop and jmp commands 
for x in range(len(input_lines)):
    tmp_lines = input_lines.copy()

    if tmp_lines[x] == 'acc':
        continue
    
    tmp_lines[x] = 'nop +0' if 'jmp' in tmp_lines[x]  else tmp_lines[x].replace("nop","jmp")
    loop_detected, acc, max_depth = run_boot_code(tmp_lines)
    # print(f"loop_detected: {loop_detected}, acc:{acc}, max_depth: {max_depth}")

    if not loop_detected:
        print(f"Part2: {acc}")
        break


