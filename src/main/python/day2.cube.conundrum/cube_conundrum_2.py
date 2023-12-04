input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def sum_minimum_cubes(text):
    lines = text.splitlines()
    result = 0
    for line in lines:
        result += sum_minimum(line)

    return result

def sum_minimum(line):
    quotation_index = line.find(":")
    subset_array = line[quotation_index + 1:].split(";")

    min_set = {}
    for subset in subset_array:
        cubes = extract_subset(subset)
        min_set = find_minimum(min_set, cubes)

    power_of_set = 0
    for value in min_set.values():
        power_of_set = (1 if power_of_set == 0 else power_of_set) * value

    return power_of_set

def find_minimum(min_dic, current_dic):
    if not min_dic:
        min_dic = current_dic

    bigger_dic = min_dic if len(min_dic) > len(current_dic) else current_dic

    for key in bigger_dic.keys():
        if current_dic.get(key, 0) > min_dic.get(key, 0):
            min_dic[key] = current_dic.get(key, 0)

    return min_dic

def extract_subset(subset):
    if not subset:
        return {}

    cubes = subset.split(",")
    dic = {}
    for cube in cubes:
        splitted = cube.strip().split(" ")
        dic[splitted[1]] = int(splitted[0])

    return dic

# print(sum_minimum_cubes(input))

f = open("./input-2.txt", "r")
text = f.read()
print(sum_minimum_cubes(text))

# print(sum_minimum("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
# print(sum_minimum("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"))
# print(sum_minimum("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"))
# print(sum_minimum("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"))
# print(sum_minimum("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"))
