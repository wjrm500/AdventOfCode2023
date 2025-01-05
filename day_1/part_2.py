import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT_FILE) as f:
    lines = f.readlines()
lines = [line.rstrip("\n") for line in lines]

number_word_to_digit_mapping = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
number_words_and_digits = list(number_word_to_digit_mapping.keys()) + list(number_word_to_digit_mapping.values())
calibration_value_sum = 0
for line in lines:
    first_found = min(
        (sub for sub in number_words_and_digits if sub in line),
        key=line.index,
    )
    first_found = number_word_to_digit_mapping.get(first_found, first_found)
    last_found = max(
        (sub for sub in number_words_and_digits if sub in line),
        key=line.rindex,
    )
    last_found = number_word_to_digit_mapping.get(last_found, last_found)
    calibration_value_sum += int(first_found + last_found)
print(calibration_value_sum)
# Answer: 54,078 - Correct