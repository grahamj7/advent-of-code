import operator


def day_7_parts_ab():
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

    sentences = open("day_7_input.txt").read().splitlines()

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

