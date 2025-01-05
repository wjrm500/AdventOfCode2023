import math
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.rstrip("\n") for line in lines]

total_points = 0
for line in lines:
    numbers = line.split(": ")[1]
    winning_numbers, actual_numbers = map(str.split, numbers.split(" | "))
    winning_number_set = set(winning_numbers)
    x = sum(n in winning_number_set for n in actual_numbers)
    points = int(math.pow(2, x - 1)) if x else 0
    total_points += points
print(total_points)
# Answer: 26,218 - Correct