import md5

def day_4_part_A():
    i = 0
    val = open('day_4_input.txt').read().splitlines()
    while True:
        x = md5.new(val+str(i)).hexdigest()
        if x.startswith("00000"):
            print x
            print i
            break
        i += 1

def day_4_part_B():
    i = 0
    val = "ckczppom"
    while True:
        x = md5.new(val+str(i)).hexdigest()
        if x.startswith("000000"):
            print x
            print i
            break
        i += 1


