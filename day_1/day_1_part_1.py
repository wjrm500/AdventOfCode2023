import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    lines = f.readlines()

calibration_value_sum = 0

for line in lines:
    first_val, second_val = None, None

    # Get first value
    for letter in line:
        if letter.isdigit():
            first_val = letter
            break
    
    # Get second value
    for letter in reversed(line):
        if letter.isdigit():
            second_val = letter
            break
    
    # Calculate calibration value
    calibration_value = int(first_val + second_val)
    
    calibration_value_sum += calibration_value

print(calibration_value_sum)
# Answer: 54,601 - Correct