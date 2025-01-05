import math
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.rstrip("\n") for line in lines]

class Scratchcard:
    card_number: int
    winning_number_set: set[int]
    actual_numbers: list[int]
    _matching_number_count: int | None

    def __init__(self, card_number: int, winning_number_set: set[int], actual_numbers: list[int]) -> None:
        self.card_number = card_number
        self.winning_number_set = winning_number_set
        self.actual_numbers = actual_numbers
        self._matching_number_count = None

    @staticmethod
    def from_input_line(line: str) -> "Scratchcard":
        card_info, numbers = line.split(": ")
        card_number = int(card_info.split()[1])
        winning_numbers, actual_numbers = map(str.split, numbers.split(" | "))
        return Scratchcard(
            card_number=card_number,
            winning_number_set=set(map(int, winning_numbers)),
            actual_numbers=list(map(int, actual_numbers)),
        )
    
    def matching_number_count(self) -> int:
        if self._matching_number_count is None:
            self._matching_number_count = len([n for n in self.actual_numbers if n in self.winning_number_set])
        return self._matching_number_count

scratchcard_data = {}
for line in lines:
    scratchcard = Scratchcard.from_input_line(line)
    scratchcard_data[scratchcard.card_number] = {
        "scratchcard": scratchcard,
        "count": 1,
    }

for card_number, scratchcard_datum in scratchcard_data.items():
    scratchcard = scratchcard_datum["scratchcard"]
    count = scratchcard_datum["count"]
    for i in range(count):
        matching_number_count = scratchcard.matching_number_count()
        for j in range(matching_number_count):
            scratchcard_number_to_copy = card_number + j + 1
            scratchcard_data[scratchcard_number_to_copy]["count"] += 1

total_count = 0
for scratchcard_datum in scratchcard_data.values():
    total_count += scratchcard_datum["count"]
print(total_count)
# Answer: 9,997,537