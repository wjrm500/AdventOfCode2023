from __future__ import annotations

import math
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.rstrip("\n") for line in lines]

class Point:
    x: int
    y: int
    value: str
    number: "Number" | None
    
    def __init__(self, x: int, y: int, value: str) -> None:
        self.x = x
        self.y = y
        self.value = value
        self.number = None
    
    def is_digit(self) -> bool:
        return self.value.isdigit()

    def is_period(self) -> bool:
        return self.value == "."

    def is_symbol(self) -> bool:
        return not self.is_digit() and not self.is_period()

    def is_adjacent_to_symbol(self, matrix: list[list["Point"]]) -> bool:
        for y in range(max(0, self.y - 1), min(len(matrix) - 1, self.y + 1) + 1):
            for x in range(max(0, self.x - 1), min(len(matrix[0]) - 1, self.x + 1) + 1):
                adjacent_point = matrix[y][x]
                if adjacent_point is self:
                    continue
                if adjacent_point.is_symbol():
                    return True
        return False
    
    def adjacent_digit_points(self, matrix: list[list["Point"]]) -> list["Point"]:
        adjacent_digit_points = []
        for y in range(max(0, self.y - 1), min(len(matrix) - 1, self.y + 1) + 1):
            for x in range(max(0, self.x - 1), min(len(matrix[0]) - 1, self.x + 1) + 1):
                adjacent_point = matrix[y][x]
                if adjacent_point is self:
                    continue
                if adjacent_point.is_digit():
                    adjacent_digit_points.append(adjacent_point)
        return adjacent_digit_points
    
    def adjacent_numbers(self, matrix: list[list["Point"]]) -> set["Number"]:
        return set(digit_point.number for digit_point in self.adjacent_digit_points(matrix))
    
    def is_gear(self, matrix: list[list["Point"]]) -> bool:
        if not self.value == "*":
            return False
        return len(self.adjacent_numbers(matrix)) == 2
    
    def gear_ratio(self, matrix: list[list["Point"]]) -> int:
        if not self.is_gear(matrix):
            return 0
        return math.prod(number.numeric_value() for number in self.adjacent_numbers(matrix))

class Number:
    points: list[Point]

    def __init__(self) -> None:
        self.points = []

    def add_point(self, point: Point) -> None:
        self.points.append(point)
        point.number = self
    
    def numeric_value(self) -> int:
        return int("".join(point.value for point in self.points))
    
    def is_part(self, matrix: list[list[Point]]) -> bool:
        return any(point.is_adjacent_to_symbol(matrix) for point in self.points)

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

gear_ratio_sum = 0
for line in matrix:
    for point in line:
        gear_ratio_sum += point.gear_ratio(matrix)
print(gear_ratio_sum)
# Answer: 73,201,705 - Correct