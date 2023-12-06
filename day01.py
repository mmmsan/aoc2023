def sumCali(lines):
    cali = []
    mapping = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'zero': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0,
    }
    for line in lines:
        indexes = []
        rindexes = []
        for key in mapping:
            index = line.find(key, 0)
            rindex = line.rfind(key, 0)
            if index >= 0:
                indexes.append((index, mapping[key]))
            if rindex >= 0:
                rindexes.append((rindex, mapping[key]))
        mindex = min(indexes)
        maxdex = max(rindexes)
        cali.append(int(str(mindex[1])+str(maxdex[1])))
    return sum(cali)

with open('input2') as f:
    lines = f.read().splitlines()

print(sumCali(lines))
