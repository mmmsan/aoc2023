import re

with open("input2") as f:
    lines = f.readlines()


def part1(lines):
    r = 12
    g = 13
    b = 14
    sum = 0
    total_power = 0
    for line in lines:
        id = int(line[:7].lstrip("Game ").rstrip(":"))
        regex = r'(\d+)\s+(\w+)'
        iterator = re.finditer(regex, line[7:])
        flag = 0
        minR = 0
        minG = 0
        minB = 0
        for match in iterator:
            if "red" in match.group():
                num = int(match.group().rstrip("red"))
                if num > minR:
                    minR = num
                if num > r:
                    flag = 1
            if "green" in match.group():
                num = int(match.group().rstrip("green"))
                if num > minG:
                    minG = num
                if num > g:
                    flag = 1
            if "blue" in match.group():
                num = int(match.group().rstrip("blue"))
                if num > minB:
                    minB = num
                if num > b:
                    flag = 1

        if flag == 0:
            sum += id

        total_power += (minR*minG*minB)

    return sum, total_power


print(part1(lines))
