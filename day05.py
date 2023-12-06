import resource
memory_limit_bytes = 14 * 1024 * 1024 * 1024 
resource.setrlimit(resource.RLIMIT_AS, (memory_limit_bytes, memory_limit_bytes))

def getInfo(lines):
    seeds1 = lines[0].split(":")[1].split() 
    seeds2 = [(seeds1[i], seeds1[i+1]) for i in range(0, len(seeds1)-1, 2)] # part 2 seeds
    seeds21 = [seeds1[i] for i in range(0, len(seeds1)-1, 2)] # part 2 stating seeds
    sts = stf = ftw = wtl = ltt = tth = htl = 0
    for index, line in enumerate(lines):
        if "seed-to-soil" in line:
            sts = index+1
        if "soil-to-fertilizer" in line:
            stf = index+1
        if "fertilizer-to-water" in line:
            ftw = index+1
        if "water-to-light" in line:
            wtl = index+1
        if "light-to-temperature" in line:
            ltt = index+1
        if "temperature-to-humidity" in line:
            tth = index+1
        if "humidity-to-location" in line:
            htl = index+1
    seeds1 = list(map(int, seeds1))
    seeds21 = list(map(int, seeds21))
    return seeds1, seeds2, seeds21, sts, stf, ftw, wtl, ltt, tth, htl


def sourceToDestination(sources, startindex, endindex, lines):
    destinations = []
    for source in sources:
        dest = 0
        for index in range(startindex, endindex):
            lower = int(lines[index].split()[1])
            base = int(lines[index].split()[0])
            upper = int(lines[index].split()[1]) + int(lines[index].split()[2])
            if lower <= source <= upper:
                dest = source - lower + base
                destinations.append(dest)
        if not dest:
            dest = source
            destinations.append(dest)
    return destinations


def getMin(seeds, sts, stf, ftw, wtl, ltt, tth, htl, lines):
    soils = sourceToDestination(seeds, sts, stf-2, lines)
    ferts = sourceToDestination(soils, stf, ftw-2, lines)
    waters = sourceToDestination(ferts, ftw, wtl-2, lines)
    lights = sourceToDestination(waters, wtl, ltt-2, lines)
    temps = sourceToDestination(lights, ltt, tth-2, lines)
    humids = sourceToDestination(temps, tth, htl-2, lines)
    locals = sourceToDestination(humids, htl, len(lines), lines)
    minLo = min(locals)
    minIndex = locals.index(minLo)
    return minLo, minIndex

# funcao para ester so a seed com min local ja

def expandMin(seeds2, minIndex):
    newseeds = []
    start, finish = seeds2[minIndex]
    start = int(start)
    finish = int(finish)
    for i in range(finish):
        seed = start + i
        newseeds.append(seed)
    return newseeds

with open("input2") as f:
    lines = f.read().splitlines()

seeds1, seeds2, seeds21, sts, stf, ftw, wtl, ltt, tth, htl =  getInfo(lines)
minLo, minIndex = getMin(seeds21, sts, stf, ftw, wtl, ltt, tth, htl, lines)
input("...")
newseeds = expandMin(seeds2, minIndex)
minLo, minIndex = getMin(newseeds, sts, stf, ftw, wtl, ltt, tth, htl, lines)
print(minLo)
