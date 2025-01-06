import math
import os
from dataclasses import dataclass, field
from enum import Enum

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    text = f.read()

class Category(str, Enum):
    SEED = "seed"
    SOIL = "soil"
    FERTILIZER = "fertilizer"
    WATER = "water"
    LIGHT = "light"
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    LOCATION = "location"

@dataclass
class RangeMap:
    source_range_start: int
    dest_range_start: int
    range_length: int


@dataclass
class Modulator:
    source_range_start: int
    source_range_end: int
    modulate_by: int

    def should_modulate(self, num: int) -> bool:
        return num >= self.source_range_start and num < self.source_range_end


@dataclass
class CategoryMap:
    source_category: Category
    dest_category: Category
    range_maps: list[RangeMap]
    _modulators: list[Modulator] = field(default=None, init=False)

    @property
    def modulators(self) -> list[Modulator]:
        if not self._modulators:
            _modulators = []
            for range_map in self.range_maps:
                source_range_end = range_map.source_range_start + range_map.range_length
                modulate_by = range_map.dest_range_start - range_map.source_range_start
                _modulators.append(
                    Modulator(
                        source_range_start=range_map.source_range_start,
                        source_range_end=source_range_end,
                        modulate_by=modulate_by,
                    )
                )
            self._modulators = _modulators
        return self._modulators
    
    def modulate_by(self, num: int) -> int:
        for modulator in self.modulators:
            if modulator.should_modulate(num):
                return modulator.modulate_by
        return 0


text_sections = text.split("\n\n")

maps_text_sections = text_sections[1:]
category_maps: list[CategoryMap] = []
for map_text_section in maps_text_sections:
    category_text, range_maps_text = map_text_section.split(":")
    source_category_text, _, dest_category_text = category_text.split()[0].split("-")
    source_category = Category(source_category_text)
    dest_category = Category(dest_category_text)
    range_maps = []
    for range_map_text in range_maps_text.strip("\n").split("\n"):
        dest_range_start_text, source_range_start_text, range_length_text = range_map_text.split()
        range_map = RangeMap(
            source_range_start=int(source_range_start_text),
            dest_range_start=int(dest_range_start_text),
            range_length=int(range_length_text),
        )
        range_maps.append(range_map)
    category_map = CategoryMap(
        source_category=source_category,
        dest_category=dest_category,
        range_maps=range_maps,
    )
    category_maps.append(category_map)

seeds_text_section = text_sections[0]
seed_values = list(map(int, seeds_text_section.split(": ")[1].split()))
lowest_location_number = math.inf
for seed_value in seed_values:
    mapped_value = seed_value
    for category_map in category_maps:
        mapped_value += category_map.modulate_by(mapped_value)
    lowest_location_number = min(lowest_location_number, mapped_value)
print(lowest_location_number)
# Answer: 318,728,750 - Correct