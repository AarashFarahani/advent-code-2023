input = """
467..114..
...*12....
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

block_pos = {0:-1, 1:0, 2:1}
def sum_part_numbers(text):
    lines = text.strip().splitlines()
    result = 0
    gear_ratios = {}
    for i in range(len(lines)):
        numbers = extract_numbers(lines[i])
        for num in numbers:
            blocks = extract_block(lines, i, num[0], num[1])
            star_position = has_star_in_block(blocks)
            if star_position:
                result += int(num[2])
                star_line = i + block_pos[star_position[0]] if i > 0 else i + star_position[0]
                star_col = num[0] + star_position[1] if num[0] == 0 else num[0] + star_position[1] - 1
                cal_star_pos = (star_line, star_col)
                g_num = gear_ratios.get(cal_star_pos, [[], 1])
                g_num[0].append(num[2])
                g_num[1] *= int(num[2])
                gear_ratios[cal_star_pos] = g_num
                print('''{} *** {}  *** {}  *** SP: {}, {}
                '''.format(i, num, star_position, star_line, star_col))

    print(gear_ratios)
    print(calculate_gear_ratios(gear_ratios))
    return result


def calculate_gear_ratios(gear_ratios):
    if not gear_ratios:
        return 0

    result = 0
    for item in gear_ratios.values():
        if len(item[0]) > 1:
            result += item[1]

    return result

def has_star_in_block(blocks):
    for i in range(len(blocks)):
        res = has_star(blocks[i])
        if res[0]:
            return [i, res[1]]

star = "*"
def has_star(str):
    for i in range(len(str)):
        if str[i] in star:
            return [True, i]

    return [False]

def extract_block(lines, index, first_index, last_index):
    if not lines[index]:
        return []

    top = index - 1 if index > 0 else 0
    bottom = index + 1 if index + 1 < len(lines) - 1 else len(lines) - 1
    left = first_index - 1 if first_index > 0 else 0
    right = last_index + 1 if last_index + 1 < len(lines[index]) - 1 else len(lines[index]) - 1

    block = []
    for i in range(top, bottom + 1):
        # if i != index:
        block.append(lines[i][left:right+1])
        # else:
        #     row = ""
        #     if left != first_index:
        #         row += lines[i][left]
        #     if right != last_index:
        #         row += lines[i][right]
        #     block.append(row)

    return block

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

f = open("./input-2.txt", "r")
result = sum_part_numbers(f.read())
print("*********************")
print(result)


# 1     81709807