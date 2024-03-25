input = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
# input = """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# 23........
# ........12
# .........%
# """

# input = """
# ..........*....511............
# ...658.509*378..........-999..
# ....*.........................
# """

# input = """
# ....*810..............34....................&....297..........#........*....................#.............899=..........972..........27.....
# 960........762.....................*........394........&355.401........347.....+853.....&...967............................*86..663.........
# ............*..........991......686.25.286.......&...................................653...........914........$.....580...........*.........
# ...#.....784......-.......*............*......498......*..........*..316........................&.&..........691.2.....*........91..........
# ..791..............462....193..........8.............57.685.......90..........201............371.....242............996................579..
# """

def sum_part_numbers(text):
    lines = text.strip().splitlines()
    result = 0
    for i in range(len(lines)):
        numbers = extract_numbers(lines[i])
        for num in numbers:
            blocks = extract_block(lines, i, num[0], num[1])
            if has_part_number(blocks):
                result += int(num[2])
                print(num[2])

    return result

def has_part_number(blocks):
    for block in blocks:
        if has_allowed_list(block):
            return block

def extract_block(lines, index, first_index, last_index):
    if not lines[index]:
        return []

    top = index - 1 if index > 0 else 0
    bottom = index + 1 if index + 1 < len(lines) - 1 else len(lines) - 1
    left = first_index - 1 if first_index > 0 else 0
    right = last_index + 1 if last_index + 1 < len(lines[index]) - 1 else len(lines[index]) - 1

    block = []
    for i in range(top, bottom + 1):
        if i != index:
            block.append(lines[i][left:right+1])
        else:
            row = ""
            if left != first_index:
                row += lines[i][left]
            if right != last_index:
                row += lines[i][right]
            block.append(row)

    return block

disallowed_list = "."
def has_allowed_list(str):
    for ch in str:
        if ch not in disallowed_list:
            return True

    return False

def extract_numbers(line):
    arr = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            first_index = i
            while i < len(line) and line[i].isdigit():
                i += 1
            arr.append((first_index, i-1, line[first_index:i]))
        else:
            i += 1

    return arr


# result = sum_part_numbers(input)
# print("****************")
# print(result)
# 4361

f = open("./input.txt", "r")
result = sum_part_numbers(f.read())
print("*********************")
print(result)

#   1   500915      Too Low
#   2   541339      Too High
#   2   538046