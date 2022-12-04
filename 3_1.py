def itemPriority(fileName):
    with open(fileName) as f:
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


        return priority


if __name__ == "__main__":
    print(itemPriority("./input/3_input.txt"))
