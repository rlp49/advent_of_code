with open("../input/2.txt") as f:
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

    print(f"part 1 {score=}")
    
    resultDict = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    gameDict = {
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
        score += gameDict[opponent][result]

    print(f"part 2 {score=}")