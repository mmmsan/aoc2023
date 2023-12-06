import math

def getWays(duration, record):
    ways = 0
    prev_attempt = 0
    for number in range(1, duration-1):  
        attempt = (duration-number)*number
        if attempt > record and attempt == prev_attempt:
            ways *= 2
            break
        elif attempt > record:
            ways += 1
            prev_attempt = attempt
    return ways

def maxWays(values):
    all_ways = []
    for i in range(len(values[0])):
        ways = getWays(int(values[0][i]), int(values[1][i]))
        all_ways.append(ways)
    return math.prod(all_ways)


with open("input2") as f:
    lines = f.read().splitlines()

values = [line.split(":")[1].split() for line in lines]
values2 = ["".join(element) for element in values]
print(f"part1: {maxWays(values)}")
print(f"part2: {getWays(int(values2[0]), int(values2[1]))}")

