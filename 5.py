from copy import deepcopy

with open("input/5_input.txt") as f:
    data = f.readlines()
    
    initial_state = [
        None,
        ["R", "G", "J", "B", "T", "V", "Z"],
        ["J", "R", "V", "L"],
        ["S", "Q", "F"],
        ["Z", "H", "N", "L", "F", "V", "Q", "G"],
        ["R", "Q", "T", "J", "C", "S", "M", "W"],
        ["S", "W", "T", "C", "H", "F"],
        ["D", "Z", "C", "V", "F", "N", "J"],
        ["L", "G", "Z", "D", "W", "R", "F", "Q"],
        ["J", "B", "W", "V", "P"]
    ]

    state = deepcopy(initial_state)

    for line in data:
        split = line.split(" ")
        quant = int(split[1])
        origin = int(split[3])
        dest = int(split[5])

        for i in range(quant):
            state[dest].append(state[origin].pop())

    ans = ""
    for i in range(1, len(state)):
        ans += state[i][-1]

    print(f"part 1 {ans=}")

    state = deepcopy(initial_state)

    print(state)

    for line in data:
        split = line.split(" ")
        quant = int(split[1])
        origin = int(split[3])
        dest = int(split[5])

        state[dest].extend(state[origin][-1 * quant:])
        state[origin] = state[origin][:-1 * quant]
    
    ans = ""
    for i in range(1, len(state)):
        ans += state[i][-1]

    print(f"part 2 {ans=}")