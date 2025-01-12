import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_example_2.txt")

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

def get_loop_positions(position: tuple[int, int], direction: str) -> set[tuple[int, int]]:
    positions = set()
    while True:
        position = (position[0] + direction[0], position[1] + direction[1])
        positions.add(position)
        if (pipe := matrix[position[0]][position[1]]) == "S":
            return positions
        direction = redirect_mapping[(direction, pipe)]

start_position = find_start_position()
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for direction in directions:
    try:
        loop_positions = get_loop_positions(start_position, direction)
        break
    except:
        continue

def escape_matrix(position: tuple[int, int], direction: tuple[int, int]) -> bool:
    while True:
        position = (position[0] + direction[0], position[1] + direction[1])
        try:
            matrix[position[0]][position[1]]
        except IndexError:
            return True # Escaped!
        if position in loop_positions:
            return False

num_positions_outside_loop = 0
for i in range(len(matrix)):
    line = matrix[i]
    for j in range(len(line)):
        position = (i, j)
        if position not in loop_positions:
            for direction in directions:
                if escape_matrix(position, direction):
                    num_positions_outside_loop += 1
                    break

num_positions = len(matrix) * len(matrix[0])
num_loop_positions = len(set(loop_positions))
num_positions_inside_loop = num_positions - num_loop_positions - num_positions_outside_loop
print(num_positions_inside_loop)