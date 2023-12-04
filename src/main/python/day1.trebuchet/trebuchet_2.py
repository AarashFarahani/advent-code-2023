text = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

def sum_calibrated_values(text):
    lines = text.splitlines()
    result = 0
    for line in lines:
        calculated = calibrate_value(line)
        print("{}   {}".format(line, calculated))
        result += calculated

    return result

def calibrate_value(line):
    if not line:
        return 0

    dic = find_digits(line)
    sum = find_first_last(dic)
    return int(sum if sum else 0)

digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
def find_digits(text):
    dic = {}
    for (key, value) in digits.items():
        index_k = text.find(key)
        index_v = text.find(value)
        index = index_k if index_k > -1 else index_v
        if index > -1:
            if index_k > -1 and index_v > -1:
                index = index_k if index_k < index_v else index_v

            dic[index] = value

        index_k = text.rfind(key)
        index_v = text.rfind(value)
        index = index_k if index_k > -1 else index_v
        if index > -1:
            if index_k > -1 and index_v > -1:
                index = index_k if index_k > index_v else index_v
            dic[index] = value

    return dic

def find_first_last(dic: dict):
    if len(dic) == 0:
        return 0

    sorted_keys = sorted(dic.keys())
    print(dic)
    first = sorted_keys[0]
    last = sorted_keys[-1]
    return (dic[first] + dic[last])

f = open("./input.txt", "r")
file = f.read()
print(sum_calibrated_values(file))
# print(sum_calibrated_values(text))
# print(calibrate_value("two1nine"))

#55614  Right Answer
#55799
#55745
#53651  53894
