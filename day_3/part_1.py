import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.rstrip("\n") for line in lines]

class Point:
    x: int
    y: int
    value: str
    
    def __init__(self, x: int, y: int, value: str) -> None:
        self.x = x
        self.y = y
        self.value = value
    
    def is_digit(self) -> bool:
        return self.value.isdigit()

    def is_period(self) -> bool:
        return self.value == "."

    def is_symbol(self) -> bool:
        return not self.is_digit() and not self.is_period()

    def symbol_adjacent(self, matrix: list[list["Point"]]) -> bool:
        for y in range(max(0, self.y - 1), min(len(matrix) - 1, self.y + 1) + 1):
            for x in range(max(0, self.x - 1), min(len(matrix[0]) - 1, self.x + 1) + 1):
                adjacent_point = matrix[y][x]
                if adjacent_point is self:
                    continue
                if adjacent_point.is_symbol():
                    return True
        return False

class Number:
    points: list[Point]

    def __init__(self) -> None:
        self.points = []

    def add_point(self, point: Point) -> None:
        self.points.append(point)
    
    def numeric_value(self) -> int:
        return int("".join(point.value for point in self.points))
    
    def is_part(self, matrix: list[list[Point]]) -> bool:
        return any(point.symbol_adjacent(matrix) for point in self.points)

matrix: list[list[Point]] = [[Point(x, y, value) for x, value in enumerate(line)] for y, line in enumerate(lines)]

numbers: list[Number] = []
current_number = None
for line in matrix:
    for point in line:
        if point.is_digit():
            if current_number is None:
                current_number = Number()
            current_number.add_point(point)
        else:
            if current_number is not None:
                numbers.append(current_number)
                current_number = None
    if current_number is not None:
        numbers.append(current_number)
        current_number = None

print(sum(number.numeric_value() for number in numbers if number.is_part(matrix)))
# Correct