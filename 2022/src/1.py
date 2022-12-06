with open("../input/1.txt") as f:
    data = f.readlines()
    highest = -1
    curr = 0
    for line in data:
        if line != "\n":
            curr += int(line)
        else:
            highest = max(curr, highest)
            curr = 0

    print(f"part 1 ans = {max(curr, highest)}")

    curr = 0
    top = [-1, -1, -1]
    for line in data:
        if line != "\n":
            curr += int(line)
        else:
            top.sort()
            top[0] = max(curr, top[0])
            curr = 0
    top.sort()
    top[0] = max(curr, top[0])
    # if -1, remove, but not needed for this file
    
    print(f"part2 ans = {sum(top)}")