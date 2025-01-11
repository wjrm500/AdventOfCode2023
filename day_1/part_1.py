import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT_FILE) as f:
    lines = f.readlines()

calibration_value_sum = 0
for line in lines:
    first_val, second_val = None, None
    for letter in line:
        if letter.isdigit():
            first_val = letter
            break
    for letter in reversed(line):
        if letter.isdigit():
            second_val = letter
            break
    calibration_value = int(first_val + second_val)
    calibration_value_sum += calibration_value

print(calibration_value_sum)
# Correct