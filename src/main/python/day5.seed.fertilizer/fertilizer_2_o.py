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
    extracted_seeds = extract_seeds(text)
    maps = extract_maps(text)
    lowest_seed_loc = None
    i = 0

    while i < len(extracted_seeds):
        # seeds = generate_list(int(extracted_seeds[i]), int(extracted_seeds[i+1]))
        # for seed in seeds:
        s = int(extracted_seeds[i])
        print(s)
        for map in maps:
            s = find_lowest_location(s, int(extracted_seeds[i+1]), map)
            print(map)
            print(s)
        i += 2
        print("*********")

        lowest_seed_loc = s if not lowest_seed_loc or s < lowest_seed_loc else lowest_seed_loc
        # lowest_seed_loc.append(s)

    return lowest_seed_loc

def find_lowest_location(seed, seed_length, list_of_maps):
    if not list_of_maps:
        return seed

    lowest = None
    for map in list_of_maps:
        source_range = map["source_range"]
        length = map["length"]
        des_range = map["des_range"]

        diff = seed - source_range
        if diff >= 0:
            if diff <= length:
                cal_low = des_range + diff
                lowest = cal_low if not lowest or cal_low < lowest else lowest
        elif diff < 0 and abs(diff) <= seed_length:
            cal_low = des_range + diff
            # cal_low = seed + (des_range - source_range)
            lowest = cal_low if not lowest or cal_low < lowest else lowest

        # diff = source_range - seed
        # if diff >= 0:
        #     if diff <= seed_length:
        #         cal_low = seed + (des_range - (source_range + diff))
        #         lowest = cal_low if not lowest or cal_low < lowest else lowest
        # elif diff < 0 and abs(diff) <= length:
        #     cal_low = seed + (des_range - source_range)
        #     lowest = cal_low if not lowest or cal_low < lowest else lowest



            # return seed + (des_range - (source_range + seed_length))
        # if seed >= source_range and seed < (source_range + length):
        #     des_range = map["des_range"]
        #     return seed + (des_range - source_range)
        # else:
        #     diff = source_range - seed
        #     if diff >= 0 and


            # max_range = (source_range + length - 1)
            # max_range_seed = (seed + length - 1)
            # if seed >= max_range
            # return find_lowest_location(seed, len)

    return lowest if lowest else seed

def extract_seeds(text):
    if not text:
        return []

    lines = text.strip().splitlines()
    seed_line = next(l for l in lines if l.startswith("seeds:"))
    return seed_line.split(":")[1].split()

def generate_list(seed, length):
    list = []
    last_seed = seed + length
    while seed < last_seed:
        list.append(seed)
        seed += 1

    return list

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
    return {"des_range": int(nums[0]), "source_range": int(nums[1]), "length": int(nums[2])}

result = find_location(input)
print("****************")
print(result)

# f = open("./input-2.txt", "r")
# result = find_location(f.read())
# print("*********************")
# print(result)

# list1 = [{'des_range': 45, 'source_range': 77, 'length': 23},
# {'des_range': 81, 'source_range': 45, 'length': 19},
# {'des_range': 68, 'source_range': 64, 'length': 13}]
# print(find_lowest_location(74, 14, list1))
#   77  48

#