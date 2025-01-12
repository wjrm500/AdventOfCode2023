import os

from shapely.geometry import Point, Polygon

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

def get_loop_positions(position: tuple[int, int], direction: str) -> list[tuple[int, int]]:
    positions = []
    while True:
        position = (position[0] + direction[0], position[1] + direction[1])
        positions.append(position)
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

loop_positions_polygon = Polygon(loop_positions)
loop_positions_set = set(loop_positions)
num_positions_inside_loop = 0
for i in range(len(matrix)):
    line = matrix[i]
    for j in range(len(line)):
        position = (i, j)
        if position not in loop_positions_set:
            if loop_positions_polygon.contains(Point(position)):
                num_positions_inside_loop += 1
print(num_positions_inside_loop)
# Correct