import math
import os
from itertools import cycle

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    input_text = f.read()

instructions, node_line_text = input_text.split("\n\n")
node_lines = node_line_text.split("\n")

instruction_cycle = cycle(instructions)

node_dict: dict[str, tuple[str]] = {}
for node_line in node_lines:
    k, v = node_line.split(" = ")
    v = tuple(v.strip("()").split(", "))
    node_dict[k] = v

start_nodes = tuple(k for k in node_dict.keys() if k.endswith("A"))
steps_by_start_node = {}
for node in start_nodes:
    steps = 0
    while not node.endswith("Z"):
        steps += 1
        instruction = next(instruction_cycle)
        idx = 1 if instruction == "R" else 0
        node = node_dict[node][idx]
    steps_by_start_node[node] = steps
print(math.lcm(*steps_by_start_node.values()))
# Correct