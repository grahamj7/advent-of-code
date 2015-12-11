

def day_9_part_b():
    sentences = open("day_9_input.txt").read().splitlines()
    dists = {}

    for sentence in sentences:
        parts = sentence.split(" ")
        first = parts[0]
        second = parts[2]
        dist = int(parts[-1])
        if dists.get(first) is None:
            dists[first] = {second: dist}
        else:
            dists[first].update({second: dist})

        if dists.get(second) is None:
            dists[second] = {first: dist}
        else:
            dists[second].update({first: dist})

    from itertools import permutations
    short_p = short_d = 10000
    for path in permutations(dists.keys()):
        x = path[0]
        dist = 0
        for y in path[1:]:
            dist += dists[x][y]
            x = y
        if short_d > dist:
            short_d = dist
            short_p = path
    print short_p, short_d

def day_9_part_b():
    sentences = open("day_9_input.txt").read().splitlines()
    dists = {}

    for sentence in sentences:
        parts = sentence.split(" ")
        first = parts[0]
        second = parts[2]
        dist = int(parts[-1])
        if dists.get(first) is None:
            dists[first] = {second: dist}
        else:
            dists[first].update({second: dist})

        if dists.get(second) is None:
            dists[second] = {first: dist}
        else:
            dists[second].update({first: dist})

    from itertools import permutations
    long_p = long_d = 0
    for path in permutations(dists.keys()):
        x = path[0]
        dist = 0
        for y in path[1:]:
            dist += dists[x][y]
            x = y
        if long_d < dist:
            long_d = dist
            long_p = path
    print long_p, long_d

