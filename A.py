
def A_A():
    f = open("1.txt").read()
    fw = len(f.split(")"))
    bw = len(f.split("("))
    print bw-fw

def A_B():
    f = open("1.txt").read()
    sum = 0
    index = 0
    for n in f:
        index += 1
        if n == "(":
            sum +=1
        else:
            sum -= 1
            if sum < 0:
                print sum, " : ", index+1
                break


def B_A():
    f = open("2.txt").read()
    list = f.split("\n")
    sum = 0
    for n in list:
        dim = n.split("x")
        if len(dim) == 3:
            dim[0] = int(dim[0])
            dim[1] = int(dim[1])
            dim[2] = int(dim[2])
            small = dim[0]*dim[1]
            if dim[1]*dim[2] < small:
                small = dim[1]*dim[2]
            if dim[0]*dim[2] < small:
                small = dim[2]*dim[0]
            total = 2*dim[0]*dim[1] + 2*dim[1]*dim[2] + 2*dim[0]*dim[2]
            total += small
            print dim
            print small
            sum += total
    print sum

def B_B():
    f = open("2.txt").read()
    list = f.split("\n")
    sum = 0
    for n in list:
        dim = n.split("x")
        if len(dim) == 3:
            dim[0] = int(dim[0])
            dim[1] = int(dim[1])
            dim[2] = int(dim[2])
            smallest = 2*(dim[0]+dim[1])
            volume = dim[0]*dim[1]*dim[2]
            if smallest > 2*(dim[0]+dim[2]):
                smallest = 2*(dim[0]+dim[2])
            if smallest > 2*(dim[1]+dim[2]):
                smallest = 2*(dim[1]+dim[2])
            total = smallest+volume
            sum += total
    print sum


def C_A():
    f = open("3.txt").read()
    houses = {}
    x = 0
    y = 0
    for n in f:
        if n == "^":
            y += 1
        elif n == "v":
            y -= 1
        elif n == "<":
            x -= 1
        elif n == ">":
            x += 1
        else:
            print "What"
        houses[str(x)+":"+str(y)] = True

    print len(houses)+1

def C_B():
    f = open("3.txt").read()
    houses = {"0:0": True}
    alt = 0
    rx = x = 0
    ry = y = 0
    for n in f:
        if alt == 0:
            if n == "^":
                y += 1
            elif n == "v":
                y -= 1
            elif n == "<":
                x -= 1
            elif n == ">":
                x += 1
            else:
                print "What"
        else:
            if n == "^":
                ry += 1
            elif n == "v":
                ry -= 1
            elif n == "<":
                rx -= 1
            elif n == ">":
                rx += 1
            else:
                print "What"
        houses[str(x)+":"+str(y)] = True
        houses[str(rx)+":"+str(ry)] = True
        alt += 1
        alt = alt % 2

    print len(houses)


def D_A():
    import md5
    i = 0
    val = "ckczppom"
    while True:
        x = md5.new(val+str(i)).hexdigest()
        if x.startswith("00000"):
            print x
            print i
            break
        i += 1

def D_B():
    import md5
    i = 0
    val = "ckczppom"
    while True:
        x = md5.new(val+str(i)).hexdigest()
        if x.startswith("000000"):
            print x
            print i
            break
        i += 1


def E_A():
    f = open("5.txt").read()
    list = f.split("\n")
    sum = 0
    vowels = ["a", "e", "i", "o", "u"]
    for word in list:
        v = 0
        double = False
        if "ab" in word:
            continue
        elif "cd" in word:
            continue
        elif "pq" in word:
            continue
        elif "xy" in word:
            continue
        for i in range(len(word)):
            if word[i] in vowels:
                v += 1
            if i != len(word)-1:
                if word[i] == word[i+1]:
                    double = True
        if v >= 3 and double:
            sum += 1

    print sum

def E_B():
    f = open("5.txt").read()
    list = f.split("\n")
    sum = 0
    for word in list:
        first = False
        # second = True
        second = False
        for i in range(len(word)-3):
            sub = word[i:i+2]
            if sub in word[i+2:]:
                first = True
                break

        for i in range(len(word)-2):
            if word[i] == word[i+2]:
                second = True
                break

        if first and second:
            sum += 1
    print sum


def F_A():
    f = open("6.txt").read()
    list = f.split("\n")
    turn = "turn"
    on = "on"
    size = 1000
    # list = ['turn on 0,0 through 2,2']
    grid = [[0 for x in range(size)] for x in range(size)]
    for sentence in list:
        parts = sentence.split(" ")
        if turn == parts[0]:
            first_set = parts[2].split(",")
            second_set = parts[4].split(",")
            if on == parts[1]:  # on
                for x in xrange(int(first_set[0]), int(second_set[0])+1):
                    for y in xrange(int(first_set[1]), int(second_set[1])+1):
                        grid[x][y] = 1
            else:  # off
                for x in xrange(int(first_set[0]), int(second_set[0])+1):
                    for y in xrange(int(first_set[1]), int(second_set[1])+1):
                        grid[x][y] = 0
        else:  # toggle
            first_set = parts[1].split(",")
            second_set = parts[3].split(",")
            for x in xrange(int(first_set[0]), int(second_set[0])+1):
                for y in xrange(int(first_set[1]), int(second_set[1])+1):
                    grid[x][y] += 1
                    grid[x][y] %= 2
    sum = 0
    for x in xrange(size):
        for y in xrange(size):
            sum += grid[x][y]

    print sum

def F_B():
    f = open("6.txt").read()
    list = f.split("\n")
    turn = "turn"
    on = "on"
    size = 1000
    grid = [[0 for x in range(size)] for x in range(size)]
    for sentence in list:
        parts = sentence.split(" ")
        if turn == parts[0]:
            first_set = parts[2].split(",")
            second_set = parts[4].split(",")
            if on == parts[1]:  # on
                for x in xrange(int(first_set[0]), int(second_set[0])+1):
                    for y in xrange(int(first_set[1]), int(second_set[1])+1):
                        grid[x][y] += 1
            else:  # off
                for x in xrange(int(first_set[0]), int(second_set[0])+1):
                    for y in xrange(int(first_set[1]), int(second_set[1])+1):
                        grid[x][y] -= 1
                        if grid[x][y] < 0:
                            grid[x][y] = 0
        else:  # toggle
            first_set = parts[1].split(",")
            second_set = parts[3].split(",")
            for x in xrange(int(first_set[0]), int(second_set[0])+1):
                for y in xrange(int(first_set[1]), int(second_set[1])+1):
                    grid[x][y] += 2
    sum = 0
    for x in xrange(size):
        for y in xrange(size):
            sum += grid[x][y]

    print sum


def G_A():
    import operator
    wires = {'0': 0, '1': 1, '2': 2, '3': 3, '5': 5, '15': 15}
    logic = {
        "AND": operator.and_,
        "OR": operator.or_,
        "RSHIFT": operator.rshift,
        "LSHIFT": operator.lshift,
        "NOT": operator.invert
    }

    def solve(key, values):
        if len(values) == 1:
            try:
                wires[key] = int(values[0])
            except:
                wires[key] = solve(values[0], wires[values[0]])
        elif len(values) == 3:
            val_0 = wires[values[0]]
            val_2 = wires[values[2]]
            try:
                val_0 = int(val_0)
            except:
                val_0 = int(solve(values[0], val_0))
            try:
                val_2 = int(val_2)
            except:
                val_2 = int(solve(values[2], val_2))

            wires[key] = logic[values[1]](val_0, val_2)

        elif len(values) == 2:
            val_1 = wires[values[1]]
            try:
                val_1 = int(val_1)
            except:
                val_1 = int(solve(values[1], val_1))

            wires[key] = logic[values[0]](val_1)

        return int(wires[key])

    f = open("7.txt").read()
    sentences = f.split("\n")

    for sentence in sentences:
        parts = sentence.split(" ")
        _key = parts[-1]
        wires[_key] = parts[:-2]

    a = solve('a', wires['a'])
    print "A: "+str(a)

    for sentence in sentences:
        parts = sentence.split(" ")
        _key = parts[-1]
        wires[_key] = parts[:-2]

    wires['b'] = a

    b = solve('a', wires['a'])
    print "B: "+str(b)


def H_A():
    sentences = open("8.txt").read().splitlines()
    code = 0
    mem = 0
    import re
    regex = re.compile(r"\\x[0-9a-f][0-9a-f]")

    for sentence in sentences:
        code += len(eval(sentence))+sentence.count("\"")+sentence.count('\\\\')+len(regex.findall(sentence))*3
        mem += len(eval(sentence))

    print code - mem

def H_B():
    sentences = open("8.txt").read().splitlines()
    new_code = 0
    code = 0
    import re
    regex = re.compile(r"\\x[0-9a-f][0-9a-f]")

    for sentence in sentences:
        count = 0
        count_quotes = 0
        count_slashes = 0

        for s in sentence:
            if s == "\"":
                print "\tquote"
                count_quotes += 2
            elif s == "\\":
                print "\tbackslash"
                count_slashes += 2
            else:
                count += 1
        total = 2+count+count_quotes+count_slashes

        new_code += total
        code += len(eval(sentence))+sentence.count("\"")+sentence.count('\\\\')+len(regex.findall(sentence))*3

    print new_code - code


def I_A():
    sentences = open("9.txt").read().splitlines()
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


def I_B():
    sentences = open("9.txt").read().splitlines()
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

def J_A(length=40):
    input_value = '3113322113'
    # input_value = '1'
    for x in range(length):
        prev = -1
        count = 1
        new_value = ''
        # print 'start: {}'.format(input_value)
        for i in input_value:
            if i == prev:
                count += 1
            else:
                if prev != -1:
                    new_value += '{}{}'.format(count, prev)
                prev = i
                count = 1
        # print '{}{}'.format(count, prev)
        new_value += '{}{}'.format(count, prev)
        input_value = new_value
        # print 'end: {}'.format(input_value)

    print len(input_value)

def J_B():
    J_A(50)







