def findThreeHighestCalories(fileName):
  with open(fileName) as f:
    data = f.readlines()
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
    return sum(top)
    
if __name__ == "__main__":
  print(findThreeHighestCalories("./input/1_input.txt"))