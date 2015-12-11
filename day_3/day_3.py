

def day_3_part_a():
    f = open("day_3_input.txt").read()
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


def day_3_part_b():
    f = open("day_3_input.txt").read()
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


