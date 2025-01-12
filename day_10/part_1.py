import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    input_text = f.read()

char_corner_mapping = {"F": "⌜", "7": "⌝", "J": "⌟", "L": "⌞"}
lines = input_text.split("\n")
matrix = [[char_corner_mapping.get(c, c) for c in line] for line in lines]

def find_start_position() -> tuple[int, int]:
    for i in range(len(matrix)):
        line = matrix[i]
        for j in range(len(line)):
            point = matrix[i][j]
            if point == "S":
                return i, j
    raise Exception("No starting point found")

direction_shift_mapping = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}

redirect_mapping = {
    ("N", "|"): "N",
    ("N", "⌜"): "E",
    ("N", "⌝"): "W",
    ("E", "-"): "E",
    ("E", "⌟"): "N",
    ("E", "⌝"): "S",
    ("S", "|"): "S",
    ("S", "⌞"): "E",
    ("S", "⌟"): "W",
    ("W", "-"): "W",
    ("W", "⌞"): "N",
    ("W", "⌜"): "S"
}

def complete_loop(position: tuple[int, int], direction: str) -> int:
    steps = 0
    while True:
        shift = direction_shift_mapping[direction]
        position = (position[0] + shift[0], position[1] + shift[1])
        steps += 1
        if (pipe := matrix[position[0]][position[1]]) == "S":
            return steps
        direction = redirect_mapping[(direction, pipe)]

start_position = find_start_position()
for direction in ["N", "E", "S", "W"]:
    try:
        steps = complete_loop(start_position, direction)
        break
    except:
        continue
print(int(steps / 2))
# Correct