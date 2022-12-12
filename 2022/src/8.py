import numpy as np

with open("../input/8.txt") as f:
    data = f.readlines()  

    treeMap = []

    for line in data:
        treeMap.append(list(map(int, list(line.strip()))))

    m = len(treeMap)
    n = len(treeMap[0])

    visibleMap = np.zeros((m, n))

    # view from left
    for i in range(m):
        highest = -1
        for j in range(n):
            if treeMap[i][j] > highest:
                highest = treeMap[i][j]
                visibleMap[i][j] = 1

    # view from right
    for i in range(m):
        highest = -1
        for j in range(n-1, -1, -1):
            if treeMap[i][j] > highest:
                highest = treeMap[i][j]
                visibleMap[i][j] = 1

    # view from top
    for j in range(n):
        highest = -1
        for i in range(m):
            if treeMap[i][j] > highest:
                highest = treeMap[i][j]
                visibleMap[i][j] = 1

    # view from bottom
    for j in range(n):
        highest = -1
        for i in range(m-1, -1, -1):
            if treeMap[i][j] > highest:
                highest = treeMap[i][j]
                visibleMap[i][j] = 1

    numVisible = sum(map(sum, visibleMap))

    print(f"part 1 {numVisible=}")

    maxVisible = 0

    # no need to check edges b/c multiply by 0
    for i in range(1, m-1):
        for j in range(1, n-1):
            up, down, left, right = 0, 0, 0, 0
            
            # looking up
            for x in range(i-1, -1, -1):
                up += 1
                if treeMap[x][j] >= treeMap[i][j]:
                    break

            # looking down
            for x in range(i+1, m):
                down += 1
                if treeMap[x][j] >= treeMap[i][j]:
                    break

            # looking left
            for y in range(j-1, -1, -1):
                left += 1
                if treeMap[i][y] >= treeMap[i][j]:
                    break

            # looking right
            for y in range(j+1, n):
                right += 1
                if treeMap[i][y] >= treeMap[i][j]:
                    break

            maxVisible = max(maxVisible, up * down * left * right)

    print(f"part 2 {maxVisible=}")

    