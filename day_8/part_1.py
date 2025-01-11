import os
from itertools import cycle

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    input_text = f.read()

instructions, node_line_text = input_text.split("\n\n")
node_lines = node_line_text.split("\n")

instruction_cycle = cycle(instructions) 

node_dict = {}
for node_line in node_lines:
    k, v = node_line.split(" = ")
    v = tuple(v.strip("()").split(", "))
    node_dict[k] = v

steps = 0
current_node = "AAA"
while current_node != "ZZZ":
    steps += 1
    instruction = next(instruction_cycle)
    idx = 1 if instruction == "R" else 0
    current_node = node_dict[current_node][idx]
print(steps)