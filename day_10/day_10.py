

def day_10_part_a(length=40):
    input_value = open('day_10_input.txt').read().splitlines()
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


def day_10_part_b():
    day_10_part_a(50)

