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
            pipe = matrix[i][j]
            if pipe == "S":
                return i, j

redirect_mapping = {
    ((-1, 0), "|"): (-1, 0),
    ((-1, 0), "⌜"): (0, 1),
    ((-1, 0), "⌝"): (0, -1),
    ((0, 1), "-"): (0, 1),
    ((0, 1), "⌟"): (-1, 0),
    ((0, 1), "⌝"): (1, 0),
    ((1, 0), "|"): (1, 0),
    ((1, 0), "⌞"): (0, 1),
    ((1, 0), "⌟"): (0, -1),
    ((0, -1), "-"): (0, -1),
    ((0, -1), "⌞"): (-1, 0),
    ((0, -1), "⌜"): (1, 0)
}

def get_loop_steps(position: tuple[int, int], direction: str) -> int:
    steps = 0
    while True:
        position = (position[0] + direction[0], position[1] + direction[1])
        steps += 1
        if (pipe := matrix[position[0]][position[1]]) == "S":
            return steps
        direction = redirect_mapping[(direction, pipe)]

start_position = find_start_position()
for direction in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    try:
        loop_steps = get_loop_steps(start_position, direction)
        break
    except:
        continue
print(int(loop_steps / 2))
# Correct