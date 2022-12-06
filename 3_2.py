def badgePriority(fileName):
    with open(fileName) as f:
        data = f.readlines()
        priority = 0

        for i in range(0, len(data), 3):
            b1 = data[i]
            b2 = data[i+1]
            b3 = data[i+2]

            for char in b1:
                if char in b2 and char in b3:
                    priority += ord(char) - ord("A") + 1 + 26 if char.isupper() else ord(char) - ord("a") + 1
                    break

        return priority


if __name__ == "__main__":
    print(badgePriority("./input/3_input.txt"))
