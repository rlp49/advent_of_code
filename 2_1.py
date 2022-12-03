def strategyScore(fileName):
    with open(fileName) as f:
        data = f.readlines()
        score = 0

        playDict = {
            'X': 1,
            'Y': 2,
            'Z': 3
        }

        winDict = {
            'A': {
                'X': 3,
                'Y': 6,
                'Z': 0
            }, 
            'B': {
                'X': 0,
                'Y': 3,
                'Z': 6
            },
            'C': {
                'X': 6,
                'Y': 0,
                'Z': 3
            },
        }

        for game in data:
            [opponent, me] = game. strip().split(' ')
            score += playDict[me]
            score += winDict[opponent][me]

        return score


if __name__ == "__main__":
    print(strategyScore("./input/2_input.txt"))
