import networkx as nx
import matplotlib.pyplot as plt

input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day10/input.txt").read().splitlines()

# input_lines = """28
# 33
# 18
# 42
# 31
# 14
# 46
# 20
# 48
# 47
# 24
# 23
# 49
# 45
# 19
# 38
# 39
# 11
# 1
# 32
# 25
# 35
# 8
# 17
# 7
# 9
# 4
# 2
# 34
# 10
# 3
# """.splitlines()
 
adapters = sorted(list(map(int, input_lines)))
adapters.insert( 0, 0) 
adapters.append( max(adapters) + 3) 

G = nx.Graph()

for idx, adapter in enumerate(adapters):
    for x in adapters[idx+1:]:
        if x - adapter in [1,2,3]:
            G.add_edge(adapter, x)
            continue
        break

# nx.draw(G)
# plt.show()
s = set(map(frozenset, nx.all_simple_paths(G, source=0, target=max(adapters))))
print(f"PART2: {len(s)}")