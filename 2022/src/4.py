with open("../input/4.txt") as f:
    data = f.readlines()

    containedPairs = 0
    overlappingPairs = 0
    
    for pair in data:
        [e1, e2] = pair.split(',')
        [e1s, e1e] = e1.split('-')
        [e2s, e2e] = e2.split('-')
        e1s, e1e, e2s, e2e = int(e1s), int(e1e), int(e2s), int(e2e)

        if (e1s >= e2s and e1e <= e2e) or (e2s >= e1s and e2e <= e1e):
            containedPairs += 1
        
        if (e1e >= e2s and e1e <= e2e) or (e2e >= e1s and e2e <= e1e):
            overlappingPairs += 1

    print(f"part 1 soln: {containedPairs=}")
    print(f"part 2 soln: {overlappingPairs=}")


    
    
    

