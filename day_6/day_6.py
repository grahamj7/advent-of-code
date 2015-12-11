

def day_6_part_a():
    list = open("day_6_input.txt").read().splitlines()
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

def day_6_part_B():
    list = open("day_6_input.txt").read().splitlines()
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


