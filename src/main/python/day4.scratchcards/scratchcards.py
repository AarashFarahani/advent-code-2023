input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

def sum_points(text):
    lines = text.strip().splitlines()
    result = 0
    for line in lines:
        result += calculate_points(extract_numbers(line))

    return result

def extract_numbers(line):
    if not line:
        return 0

    numbers = line.split(":")
    return numbers[1].split("|")

def calculate_points(numbers_str):
    if not numbers_str or len(numbers_str) <= 1 or not numbers_str[0] or not numbers_str[1]:
        return 0

    winning_numbers = string_to_numbers(numbers_str[0])
    my_numbers = string_to_numbers(numbers_str[1])
    list_of_matched = matching_numbers(winning_numbers, my_numbers)
    if not list_of_matched:
        return 0

    print(list_of_matched)
    result = 1
    for i in range(len(list_of_matched) - 1):
        result *= 2

    print(result)
    return result

def string_to_numbers(string):
    if not string:
        return

    list = []
    for num in string.split(" "):
        n = str_to_num(num)
        if n:
            list.append(n)

    return list

def str_to_num(num):
    if not num or not num.strip():
        return

    return int(num)

def matching_numbers(winning_numbers, my_numbers):
    list = []
    for num in winning_numbers:
        if num in my_numbers:
            list.append(num)

    return list

# result = sum_points(input)
# print("****************")
# print(result)
#

f = open("./input.txt", "r")
result = sum_points(f.read())
print("*********************")
print(result)

#   32609