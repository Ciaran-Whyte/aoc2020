from anytree import Node, RenderTree, PreOrderIter
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

def build_tree(node: Node):
    node_line=re.search('{} bags contain.*'.format(node.name), input_lines).group()
    for leaf in re.findall('(\d) (\w+ \w+) bag', node_line):
        build_tree(Node(leaf[1], parent=node, v=int(leaf[0])))

def sum_childern(node):
    running_total=0
    for child in node.children:
        running_total+=(child.v + (child.v * sum_childern(child)))
    return running_total

root=Node('shiny gold', v=1)
build_tree(root)

for pre, fill, node in RenderTree(root):
    print("%s%s:  %d" % (pre, node.name, node.v))

print(f"PART2: {sum_childern(root)}")


# (venv) *[main][~/dev/aoc2020]$ python day7/part2.py
# shiny gold:  1
# ├── light black:  5
# │   ├── posh coral:  1
# │   │   └── dark tomato:  3
# │   │       ├── light gray:  3
# │   │       ├── dull cyan:  2
# │   │       ├── striped silver:  4
# │   │       └── dark fuchsia:  5
# │   ├── dotted black:  4
# │   │   └── vibrant white:  2
# │   │       ├── muted green:  3
# │   │       │   ├── striped silver:  5
# │   │       │   └── bright orange:  5
# │   │       └── bright tomato:  2
# │   │           ├── muted green:  2
# │   │           │   ├── striped silver:  5
# │   │           │   └── bright orange:  5
# │   │           └── light olive:  1
# │   │               └── striped turquoise:  4
# │   ├── posh lime:  4
# │   │   ├── mirrored yellow:  5
# │   │   │   └── light olive:  4
# │   │   │       └── striped turquoise:  4
# │   │   └── striped silver:  1
# │   └── bright blue:  4
# │       ├── posh silver:  5
# │       ├── dull cyan:  4
# │       ├── light olive:  4
# │       │   └── striped turquoise:  4
# │       └── mirrored white:  1
# ├── mirrored yellow:  3
# │   └── light olive:  4
# │       └── striped turquoise:  4
# └── muted plum:  5
# PART2: 6683