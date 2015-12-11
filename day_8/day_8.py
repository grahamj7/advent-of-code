import re


def day_8_part_a():
    sentences = open("day_8_input.txt").read().splitlines()
    code = 0
    mem = 0
    regex = re.compile(r"\\x[0-9a-f][0-9a-f]")

    for sentence in sentences:
        code += len(eval(sentence))+sentence.count("\"")+sentence.count('\\\\')+len(regex.findall(sentence))*3
        mem += len(eval(sentence))

    print code - mem

def day_8_part_b():
    sentences = open("day_8_input.txt").read().splitlines()
    new_code = 0
    code = 0
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
