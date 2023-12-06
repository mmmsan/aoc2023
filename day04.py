def getPoints(lines):
    total_points = 0
    for index, line in enumerate(lines):
        winnum = set(filter(None, lines[index].split(
            ":")[1].split("|")[0].split(" ")))
        mynum = set(filter(None, lines[index].split(
            ":")[1].split("|")[1].split(" ")))
        inter = winnum.intersection(mynum)
        points = 2**len(inter)//2
        total_points += points

    return total_points


def getCards(lines, weights):
    index = 0
    total_iterations = 0
    while index < len(lines):
        total_iterations += 1
        winnum = set(filter(None, lines[index].split(
            ":")[1].split("|")[0].split(" ")))
        mynum = set(filter(None, lines[index].split(
            ":")[1].split("|")[1].split(" ")))
        hits = len(winnum.intersection(mynum))
        if hits:
            for i in range(index+1, index+1+hits):
                weights[i] += 1
        weights[index] -= 1
        if weights[index] == 0:
            index += 1
    return total_iterations


with open("input") as f:
    lines = f.read().splitlines()  # Getting lines without /n
    weights = [1] * len(lines)

points = (getPoints(lines))
cards = getCards(lines, weights)
print(f"Total points: {points} \nTotal cards: {cards}")
