

def day_1_part_a():
    f = open("day_1_input.txt").read()
    fw = len(f.split(")"))
    bw = len(f.split("("))
    print bw-fw


def day_1_part_b():
    f = open("day_1_input.txt").read()
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

