import os
from enum import Enum

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT_FILE) as f:
    games = f.readlines()

games = [game.rstrip("\n") for game in games]

MAX_CUBES_BY_COLOUR = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def is_game_record_possible(game_record: str) -> bool:
    handfuls = [tuple(x.split(", ")) for x in game_record.split("; ")]
    for handful in handfuls:
        for cube_set in handful:
            num_cubes, colour = cube_set.split()
            if int(num_cubes) > MAX_CUBES_BY_COLOUR[colour]:
                return False
    return True

id_sum = 0
for game in games:
    game_intro, game_record = game.split(": ")
    game_id = int(game_intro.split()[1])
    id_sum += game_id if is_game_record_possible(game_record) else 0
print(id_sum)
# Answer: 2,164 - Correct