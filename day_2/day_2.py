
def day_2_part_a():
    list = open("day_2_input.txt").read().splitlines()
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


def day_2_part_b():
    list = open("day_2_input.txt").read().splitlines()
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
