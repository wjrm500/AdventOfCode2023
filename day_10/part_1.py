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

def complete_loop(position: tuple[int, int], direction: str) -> int:
    steps = 0
    while True:
        shift = direction_shift_mapping[direction]
        next_pipe = matrix[position[0] + shift[0]][position[1] + shift[1]]
        position = (position[0] + shift[0], position[1] + shift[1])
        steps += 1
        if next_pipe == "S":
            return steps
        if direction == "N":
            if next_pipe == "|":
                continue
            elif next_pipe == "⌜":
                direction = "E"
                continue
            elif next_pipe == "⌝":
                direction = "W"
                continue
            else:
                raise Exception("Loop failed")
        elif direction == "E":
            if next_pipe == "-":
                continue
            elif next_pipe == "⌟":
                direction = "N"
                continue
            elif next_pipe == "⌝":
                direction = "S"
                continue
            else:
                raise Exception("Loop failed")
        elif direction == "S":
            if next_pipe == "|":
                continue
            elif next_pipe == "⌞":
                direction = "E"
                continue
            elif next_pipe == "⌟":
                direction = "W"
                continue
            else:
                raise Exception("Loop failed")
        elif direction == "W":
            if next_pipe == "-":
                continue
            elif next_pipe == "⌞":
                direction = "N"
                continue
            elif next_pipe == "⌜":
                direction = "S"
                continue
            else:
                raise Exception("Loop failed")

start_position = find_start_position()
for direction in ["N", "E", "S", "W"]:
    try:
        steps = complete_loop(start_position, direction)
        break
    except:
        continue
print(int(steps / 2))
# Correct