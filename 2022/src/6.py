with open("../input/6.txt") as f:
    data = f.readlines()[0]
    
    a, b = 0, 4
    while b <= len(data):
        if len(set(data[a:b])) == 4:
            break
        else:
            a += 1
            b += 1
    
    print(f"part 1 ans={b}")

    a, b = 0, 14
    while b <= len(data):
        if len(set(data[a:b])) == 14:
            break
        else:
            a += 1
            b += 1
    
    print(f"part 2 ans={b}")