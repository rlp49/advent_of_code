with open("../input/3.txt") as f:
    data = f.readlines()

    mistakes = list()

    for rucksack in data:
        c1 = rucksack[:len(rucksack) // 2]
        c2 = rucksack[len(rucksack) // 2 : ]
        for char in set(c1):
            if c2.count(char) > 0:
                mistakes.append(char)

    priority = 0

    for mistake in mistakes:
        if mistake.isupper():
            priority += ord(mistake) - ord("A") + 1 + 26
        else:
            priority += ord(mistake) - ord("a") + 1


    print(f"part 1 {priority=}")

    priority = 0

    for i in range(0, len(data), 3):
        b1 = data[i]
        b2 = data[i+1]
        b3 = data[i+2]

        for char in b1:
            if char in b2 and char in b3:
                priority += ord(char) - ord("A") + 1 + 26 if char.isupper() else ord(char) - ord("a") + 1
                break

    print(f"part 2 {priority=}")