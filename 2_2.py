def strategyScore(fileName):
    with open(fileName) as f:
        data = f.readlines()
        score = 0

        resultDict = {
            'X': 0,
            'Y': 3,
            'Z': 6
        }

        playDict = {
            'A': {
                'X': 3,
                'Y': 1,
                'Z': 2
            }, 
            'B': {
                'X': 1,
                'Y': 2,
                'Z': 3
            },
            'C': {
                'X': 2,
                'Y': 3,
                'Z': 1
            },
        }

        for game in data:
            [opponent, result] = game. strip().split(' ')
            score += resultDict[result]
            score += playDict[opponent][result]

        return score


if __name__ == "__main__":
    print(strategyScore("./input/2_input.txt"))
