import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    input_text = f.read()

def evaluate(sequence: list[int]) -> int:
    if all(x == 0 for x in sequence):
        return 0
    new_sequence = [pair[1] - pair[0] for pair in zip(sequence, sequence[1:])] 
    return sequence[0] - evaluate(new_sequence)

input_lines = input_text.split("\n")
input_sequences = [list(map(int, line.split())) for line in input_lines]
sum = sum(evaluate(i) for i in input_sequences)
print(sum)
# Correct