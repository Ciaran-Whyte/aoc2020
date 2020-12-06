input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day6/input.txt").read()
# input_lines = """abc

# a
# b
# c

# ab
# ac

# a
# a
# a
# a

# b
# """
 
print("PART1: {}".format(sum([len(set(''.join(declaration_form.splitlines()))) for declaration_form in input_lines.split('\n\n')])))

total=0
for group_answers in [list(map(set,declaration_form.split())) for declaration_form in input_lines.split('\n\n')]:
    the_rest = group_answers[1:] if len(group_answers) else [set()]
    total+=len(group_answers[0].intersection(*the_rest))

print(f"PART2: {total}")







