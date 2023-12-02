with open("input") as f:
    lines = f.readlines()


def part1(lines):

    sum = 0
    set = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")

    for line in lines:
        only_nums = []
        for i in range(len(line)):
            if line[i] in set:
                only_nums.append(line[i])
        sum += int(only_nums[0]+only_nums[-1])

    return sum


def part2(lines):

    set = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
    sum = 0

    for line in lines:
        nums = []

        for i in range(len(line)):
            if line[i] in set:
                nums.append(f"{i}, {line[i]}")

        if "one" in line:
            nums.append(f"{line.index('one')}, 1")
        if "two" in line:
            nums.append(f"{line.index('two')}, 2")
        if "three" in line:
            nums.append(f"{line.index('three')}, 3")
        if "four" in line:
            nums.append(f"{line.index('four')}, 4")
        if "five" in line:
            nums.append(f"{line.index('five')}, 5")
        if "six" in line:
            nums.append(f"{line.index('six')}, 6")
        if "seven" in line:
            nums.append(f"{line.index('seven')}, 7")
        if "eight" in line:
            nums.append(f"{line.index('eight')}, 8")
        if "nine" in line:
            nums.append(f"{line.index('nine')}, 9")
        if "zero" in line:
            nums.append(f"{line.index('zero')}, 0")

        sorted_nums = sorted(nums, key=lambda pair: int(pair.split(",")[0]))
        first = sorted_nums[0].split(",")[1]
        last = sorted_nums[-1].split(",")[1]
        number = (10 * int(first)) + int(last)
        sum += number

    return sum


print(part2(lines))
