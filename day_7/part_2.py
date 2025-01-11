import os
from collections import Counter

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    lines = f.readlines()

lines = [line.rstrip("\n") for line in lines]

class Hand:
    card_str: str
    card_values: list[str]
    _hand_type: tuple[int] | None = None

    CARD_VALUES = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 1,
        "T": 10,
    }

    def __init__(self, card_str: str) -> None:
        self.card_str = card_str
        self.card_values = [int(self.CARD_VALUES.get(l, l)) for l in card_str]
    
    def __lt__(self, other: "Hand") -> bool:
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for self_card, other_card in zip(self.card_values, other.card_values):
            if self_card != other_card:
                return self_card < other_card
        return False
    
    @property
    def hand_type(self) -> tuple[int]:
        joker_count = self.card_values.count(1)
        card_values_sans_jokers = [v for v in self.card_values if v != 1]
        if not self._hand_type:
            most_common = Counter(card_values_sans_jokers).most_common(2)
            try:
                self._hand_type = most_common[0][1] + joker_count, most_common[1][1]
            except IndexError:
                self._hand_type = (5, 0)
        return self._hand_type

hand_bids: list[tuple[Hand, int]] = []
for line in lines:
    card_str, bid = line.split()
    hand = Hand(card_str)
    hand_bids.append((hand, int(bid)))
hand_bids.sort(key=lambda x: x[0])
print(sum(i * hand_bid[1] for i, hand_bid in enumerate(hand_bids, 1)))
# Correct