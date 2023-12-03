import math


def solve(lines):
    total_sum = 0
    ratios = []
    forb = (".", "\n")
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if not char.isdigit() and char not in forb:
                adj_numbers = []  # Using a list to capture adjacent numbers
                adjacent_positions = [  # Adj positions in a square
                    (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
                for dx, dy in adjacent_positions:
                    ni, nj = i + dx, j + dy  # Maps in relation to char
                    # Checking if ni and nj does not IndexError and current is a digit
                    bounded = 0 <= ni < len(lines) and 0 <= nj < len(line)
                    aux = []
                    llen = len(lines)
                    if bounded and lines[ni][nj].isdigit() and dy == -1:
                        readLeft(aux, ni, nj, line, lines, llen)
                        readRight(aux, ni, nj+1, line, lines, llen)
                        if aux:
                            adj_numbers.append(int(''.join(aux)))
                    elif bounded and lines[ni][nj].isdigit() and not lines[ni][nj-1].isdigit():
                        readLeft(aux, ni, nj, line, lines, llen)
                        readRight(aux, ni, nj+1, line, lines, llen)
                        if aux:
                            adj_numbers.append(int(''.join(aux)))

                if char == "*" and len(adj_numbers) == 2:
                    ratios.append(math.prod(adj_numbers))

                total_sum += sum(adj_numbers)

    ratio_sum = sum(ratios)
    return total_sum, ratio_sum


def readLeft(aux, ti, tj, line, lines, llen):
    while lines[ti][tj].isdigit():
        aux.insert(0, lines[ti][tj])  # reads left, inserts at start
        tj -= 1
    return aux


def readRight(aux, ti, tj, line, lines, llen):
    while lines[ti][tj].isdigit():
        aux.append(lines[ti][tj])  # reads right, appends
        tj += 1
    return aux


with open("input2") as f:
    lines = f.readlines()

part1, part2 = solve(lines)
print(f"Sum of part numbers: {part1} \nSum of gear ratios: {part2}")
