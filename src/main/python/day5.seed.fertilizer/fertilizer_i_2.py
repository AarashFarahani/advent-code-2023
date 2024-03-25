input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
# input = """
# seeds: 74 14
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
# """

import re
import math

class GardinerMap():
    source_type: str
    dest_type: str

    src_ranges: list[tuple[int, int]] = field(default_factory=list)  # [(src_start, length), (src_start, length), ... ]
    dest_ranges: list[tuple[int, int]] = field(
        default_factory=list)  # [(dest_start, length), (dest_start, length), ... ]

    def add_range(self, src_start: int, dest_start: int, range_length: int):
        """ Add a range which contains src start, dest start, and the length of the range """
        self.src_ranges.append((src_start, range_length))
        self.dest_ranges.append((dest_start, range_length))

    def _sort_ranges(self):
        """ Sort the range into ascending numeric, based on source range start values """

        # Sort src_ranges and get the order of indices
        index_order = sorted(range(len(self.src_ranges)), key=lambda i: self.src_ranges[i][0])

        # Now sort both ranges
        self.src_ranges = [self.src_ranges[i] for i in index_order]
        self.dest_ranges = [self.dest_ranges[i] for i in index_order]

    def finalise(self):
        """ Sort the range into ascending numeric, based on source range start values """
        self._sort_ranges()

    def get_target(self, src_val: int):
        """ Map a source value to a target value """
        target = src_val  # if our source isn't in a range, then return the same value

        for i, curr_range in enumerate(self.src_ranges):
            src_start = curr_range[0]
            src_end = curr_range[0] + curr_range[1]  # exclusive end
            if src_start <= src_val < src_end:  # if our source is in a range, then apply the shift
                target = src_val - src_start + self.dest_ranges[i][0]
                break  # we've mapped the value, so no more ranges need to be checked

        return target

    # For Part 2
    def map_intervals(self, src_intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
        """
        Take input ranges and return output ranges.
        - src_ranges: [(rng1_start, rng1_end), (rng2_start, rng2_end), ... ]
        """
        new_intervals = []

        # Iterate through the ranges, just as we did when mapping a single seed
        for i, curr_range in enumerate(self.src_ranges):
            src_start = curr_range[0]
            src_end = curr_range[0] + curr_range[1]  # exclusive end
            dest = self.dest_ranges[i][0]

            temp_intervals = []

            while src_intervals:  # process the current interval
                (int_start, int_end) = src_intervals.pop()

                # Split the interval using the ranges in our map
                #### Scenario 1: ####
                # [int_start                                  int_end]
                #            [src_start      src_end]
                # [left     ][mid                   ][right          ]
                #
                #### Scenario 2: ####
                #                [int_start         int_end]
                #   [src_start     src_end]
                #   [n/a        ][mid     ][right          ]
                left = (int_start, min(int_end, src_start))
                mid = (max(int_start, src_start), min(src_end, int_end))
                right = (max(src_end, int_start), int_end)

                if left[1] > left[0]:  # if left has +ve length, then scenario 1, else scenario 2
                    temp_intervals.append(left)  # pass on the interval unchanged
                if mid[1] > mid[0]:  # if mid has +ve length, then we need to apply the shift to this interval
                    # furthermore, once mapped, we know this interval wont appear in another range
                    new_intervals.append((mid[0] - src_start + dest, mid[1] - src_start + dest))
                if right[1] > right[0]:  # if right has +ve length
                    temp_intervals.append(right)  # pass on the interval unchanged

            src_intervals = temp_intervals

        return new_intervals + src_intervals

def parse_data(data: list[str]) -> tuple[list[int], list[GardinerMap]]:
    """ Parse input data, and convert to:
    - seeds: list of int
    - GardinerMap instances: list of GardinerMap """

    seeds = []
    source_maps = []  # Store our GardinerMap instances

    # Process the input file line by line, and switch modes based on the line last read
    current_map = None
    for line in data:
        if line.startswith("seeds"):  # The first line contains the seeds values
            _, seeds_part = line.split(":")
            seeds = [int(x) for x in seeds_part.split()]
        elif "map:" in line:  # start of a map block; enter map processing mode
            map_src, _, map_dest = line.split()[0].split("-")
            current_map = GardinerMap(map_src, map_dest)  # initialise our GardinerMap
        elif not line:  # empty line, so finish with the current_map and add it to our list of GardinerMaps
            if current_map:
                current_map.finalise()
                source_maps.append(current_map)  # add it to the list
                current_map = None  # and ensure we're no longer in map processing mode
        else:  # we're in map processing mode
            assert line[0].isdigit(), "Line must start with numbers"
            assert current_map, "We must be adding to a Map now"
            dest_start, src_start, interval_len = [int(x) for x in line.split()]
            current_map.add_range(src_start=src_start, dest_start=dest_start, range_length=interval_len)

    # We don't read a final empty line at the end of the input, but I still want to finalise the block
    if current_map:  # process the final map
        current_map.finalise()
        source_maps.append(current_map)  # add it to the dict

    return seeds, source_maps


def solve_part2(data):
    location_map = {}
    seeds, source_maps = parse_data(data)

    # convert seeds to intervals, of format [(start, end), ...] where end is exclusive
    # let's call them intervals, to avoid confusion with the ranges we stored in our GardinerMap
    seed_intervals = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    current_intervals = seed_intervals
    for current_map in source_maps:
        current_intervals = current_map.map_intervals(current_intervals)

    return min(start for start, _ in current_intervals)


# result = find_location(input)
# print("****************")
# print(result)

# print(find_location(input))

# f = open("./input-2.txt", "r")
# result = find_location(f.read())
# print("*********************")
# print(result)


#