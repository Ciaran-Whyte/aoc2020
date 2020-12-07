import re
input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day7/input.txt").read()
# input_lines = """light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.
# """
 
bag_regex='(.*) bags contain.*\d {} bag'

stack=['shiny gold']
total=0
bags=set()
while len(stack) > 0:
    current_bag=stack.pop()
    parent_bags = re.findall(bag_regex.format(current_bag), input_lines)
    stack.extend(parent_bags)
    
    for x in parent_bags:
        bags.add(x) 

print(f"PART 1: {len(bags)}")
