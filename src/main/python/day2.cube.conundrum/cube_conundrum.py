configuration = {"red": 12, "green": 13, "blue": 14}
input = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def sum_possible_cubes(text):
    lines = text.splitlines()
    result = 0
    for line in lines:
        result += sum_possible_games(line)

    return result

def sum_possible_games(line):
    if not line:
        return 0

    game_id = int(extract_game(line))
    return game_id if is_possible(line) else 0

def extract_game(line):
    quotation_index = line.find(":")
    return line[:quotation_index].split(" ")[1]

def is_possible(line):
    quotation_index = line.find(":")
    subset_array = line[quotation_index + 1:].split(";")

    for subset in subset_array:
        cubes = extract_subset(subset)
        if not is_match(cubes):
            return False

    return True

def is_match(cubes):
    for key, value in configuration.items():
        if int(cubes.get(key, 0)) > value:
            return False

    return True

def extract_subset(subset):
    if not subset:
        return {}

    cubes = subset.split(",")
    dic = {}
    for cube in cubes:
        splitted = cube.strip().split(" ")
        dic[splitted[1]] = splitted[0]

    return dic

print(sum_possible_cubes(input))

f = open("./input.txt", "r")
text = f.read()
print(sum_possible_cubes(text))
# print(is_possible("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
# print(is_possible("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"))
# print(is_possible("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"))
# print(is_possible("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"))
# print(is_possible("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"))