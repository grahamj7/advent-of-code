

def day_5_part_a():
    list = open("day_5_input.txt").read().splitlines()
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


def day_5_part_b():
    list = open("day_5_input.txt").read().splitlines()
    sum = 0
    for word in list:
        first = False
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


