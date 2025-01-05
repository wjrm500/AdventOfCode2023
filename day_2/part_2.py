import math
import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")

with open(INPUT_FILE) as f:
    games = f.readlines()

games = [game.rstrip("\n") for game in games]

def power(game_record: str) -> bool:
    MIN_CUBES_REQUIRED = {"red": 0, "green": 0, "blue": 0}
    handfuls = [tuple(x.split(", ")) for x in game_record.split("; ")]
    for handful in handfuls:
        for cube_set in handful:
            num_cubes, colour = cube_set.split()
            MIN_CUBES_REQUIRED[colour] = max(MIN_CUBES_REQUIRED[colour], int(num_cubes))
    return math.prod(MIN_CUBES_REQUIRED.values())

power_sum = 0
for game in games:
    game_record = game.split(": ")[1]
    power_sum += power(game_record)
print(power_sum)
# Answer: 69,929 - Correct