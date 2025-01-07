import math
import os
from dataclasses import dataclass, field

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input_test.txt")

with open(INPUT_FILE) as f:
    text = f.read()


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


@dataclass
class CategoryMap:
    range_maps: list[RangeMap]
    _modulators: list[Modulator] | None = field(default=None, init=False)

    @property
    def modulators(self) -> list[Modulator]:
        if not self._modulators:
            gappy_modulators: list[Modulator] = []
            for range_map in self.range_maps:
                source_range_end = range_map.source_range_start + range_map.range_length
                modulate_by = range_map.dest_range_start - range_map.source_range_start
                gappy_modulators.append(
                    Modulator(
                        source_range_start=range_map.source_range_start,
                        source_range_end=source_range_end,
                        modulate_by=modulate_by,
                    )
                )
            gappy_modulators = sorted(gappy_modulators, key=lambda m: m.source_range_start)
            gap_free_modulators: list[Modulator] = []

            # Fill in gaps between modulators
            for i in range(len(gappy_modulators) - 1):
                if i == 0:
                    gap_free_modulators.append(gappy_modulators[i])
                if gappy_modulators[i + 1].source_range_start > gappy_modulators[i].source_range_end:
                    new_modulator = Modulator(
                        source_range_start=gappy_modulators[i].source_range_end,
                        source_range_end=gappy_modulators[i + 1].source_range_start,
                        modulate_by=0,
                    )
                    gap_free_modulators.append(new_modulator)
                gap_free_modulators.append(gappy_modulators[i + 1])
            
            # Add initial modulator starting at 0
            if gap_free_modulators[0].source_range_start > 0:
                initial_modulator = Modulator(
                    source_range_start=0,
                    source_range_end=gap_free_modulators[0].source_range_start,
                    modulate_by=0
                )
                gap_free_modulators.insert(0, initial_modulator)
            
            # Add final modulator ending at infinity
            final_modulator = Modulator(
                source_range_start=gap_free_modulators[-1].source_range_end,
                source_range_end=math.inf,
                modulate_by=0,
            )
            gap_free_modulators.append(final_modulator)

            self._modulators = gap_free_modulators
        return self._modulators
    
    def map_ranges(self, ranges: list[range]) -> list[range]:
        new_ranges = []
        for range_ in ranges:
            for modulator in self.modulators:
                range_overlap = range(
                    max(range_.start, modulator.source_range_start),
                    min(range_.stop, modulator.source_range_end),
                )
                if range_overlap.stop > range_overlap.start:
                    transformed_start = range_overlap.start + modulator.modulate_by
                    transformed_end = range_overlap.stop + modulator.modulate_by
                    new_ranges.append(range(transformed_start, transformed_end))
        return new_ranges


text_sections = text.split("\n\n")

maps_text_sections = text_sections[1:]
category_maps: list[CategoryMap] = []
for map_text_section in maps_text_sections:
    range_maps_text = map_text_section.split(":")[1]
    range_maps = []
    for range_map_text in range_maps_text.strip("\n").split("\n"):
        dest_range_start_text, source_range_start_text, range_length_text = range_map_text.split()
        range_map = RangeMap(
            source_range_start=int(source_range_start_text),
            dest_range_start=int(dest_range_start_text),
            range_length=int(range_length_text),
        )
        range_maps.append(range_map)
    category_map = CategoryMap(range_maps=range_maps)
    category_maps.append(category_map)

seeds_text_section = text_sections[0]
seed_numbers = list(map(int, seeds_text_section.split(": ")[1].split()))
seed_ranges: list[range] = []
for i in range(0, len(seed_numbers) - 1, 2):
    seed_range = range(
        seed_numbers[i],
        seed_numbers[i] + seed_numbers[i + 1],
    )
    seed_ranges.append(seed_range)

mapped_ranges = seed_ranges
for category_map in category_maps:
    mapped_ranges = category_map.map_ranges(mapped_ranges)

lowest_location_number_overall = min(range_.start for range_ in mapped_ranges)
print(lowest_location_number_overall)