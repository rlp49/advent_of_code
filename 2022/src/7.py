from collections import defaultdict



with open("../input/7.txt") as f:
    data = f.readlines()  

    curr = ["/."]
    contains = defaultdict(lambda: [0])
    dSize = {}

    for line in data:
        split = line.strip().split(' ')
        match split[0]:
            case "$":
                if split[1] == "cd":
                    match split[2]:
                        case "/":
                            curr = ["/."]
                        case "..":
                            curr.pop()
                        case _:
                            curr.append(split[2])
            case "dir":
                contains["/".join(curr)].append("/".join(curr + [split[1]]))
            case _: # split[0] = file size
                contains["/".join(curr)][0] += int(split[0])

    def sumUp(d):
        s = 0
        for obj in contains[d]:
            if type(obj) is int:
                s += obj
            else:
                if obj not in dSize:
                    sumUp(obj)
                s += dSize[obj]
        dSize[d] = s

    sumUp("/.")

    ans = sum([v for v in dSize.values() if v <= 100000])
 
    print(f"part 1 {ans=}")

    diskSize = 70000000
    needToFree = dSize["/."] - 40000000

    ans = 999999999999
    for v in dSize.values():
        if v >= needToFree:
            ans = min(ans, v)

    print(f"part 2 {ans=}")