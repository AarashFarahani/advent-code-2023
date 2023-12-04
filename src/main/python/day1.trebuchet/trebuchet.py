text = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

def sum_calibrated_values(text):
    lines = text.splitlines()
    result = 0
    for line in lines:
        result += calibrate_value(line)

    return result

def calibrate_value(line):
    if not line:
        return 0

    first, last = "", ""

    for c in line:
        if c.isdigit():
            if not first:
                first = c
            else:
                last = c

    sum = (first + last)
    sum = (sum + first) if first and not last else sum
    return int(sum if sum else 0)

print(sum_calibrated_values(text))

f = open("./input.txt", "r")
text = f.read()
print(sum_calibrated_values(text))

# print(calibrate_value("1abc2"))
# print(calibrate_value("pqr3stu8vwx"))
# print(calibrate_value("a1b2c3d4e5f"))
# print(calibrate_value("treb7uchet"))
#
# print(calibrate_value("1aaf2tt"))
# print(calibrate_value("arash"))
# print(calibrate_value(""))
