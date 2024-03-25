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

def find_location(text):
    seeds = extract_seeds(text)
    maps = extract_maps(text)
    lowest_seed_loc = []

    for seed in seeds:
        s = int(seed)
        for map in maps:
            s = find_lowest_location(s, map)
            print(s)
        lowest_seed_loc.append(s)
        print("****************")

    return min(lowest_seed_loc)

def find_lowest_location(seed, list_of_maps):
    if not list_of_maps:
        return seed

    for map in list_of_maps:
        source_range = map["source_range"]
        length = map["length"]

        if seed > source_range and seed < (source_range + length):
            dest_range = map["dest_range"]
            return seed + (dest_range - source_range)

    return seed

def extract_seeds(text):
    if not text:
        return []

    lines = text.strip().splitlines()
    seed_line = next(l for l in lines if l.startswith("seeds:"))
    return seed_line.split(":")[1].split()

def find_line_index(text, map_name):
    if not text:
        return

    lines = text.strip().splitlines()
    for i in range(len(lines)):
        if lines[i].startswith(map_name):
            return i

def extract_maps(text):
    maps = []
    maps.append(extract_map(text, find_line_index(text, "seed-to-soil map:")))
    maps.append(extract_map(text, find_line_index(text, "soil-to-fertilizer map:")))
    maps.append(extract_map(text, find_line_index(text, "fertilizer-to-water map:")))
    maps.append(extract_map(text, find_line_index(text, "water-to-light map:")))
    maps.append(extract_map(text, find_line_index(text, "light-to-temperature map:")))
    maps.append(extract_map(text, find_line_index(text, "temperature-to-humidity map:")))
    maps.append(extract_map(text, find_line_index(text, "humidity-to-location map:")))

    return maps

def extract_map(text, map_index):
    if not text:
        return []

    map = []
    lines = text.strip().splitlines()
    while map_index + 1 < len(lines):
        map_index += 1
        if not lines[map_index]:
            break

        map.append(convert_to_map(lines[map_index]))

    return map

def convert_to_map(line):
    nums = line.split()
    return {"dest_range": int(nums[0]), "source_range": int(nums[1]), "length": int(nums[2])}

result = find_location(input)
print("****************")
print(result)

# f = open("./input.txt", "r")
# result = find_location(f.read())
# print("*********************")
# print(result)


#   382895070