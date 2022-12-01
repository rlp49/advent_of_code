def findHighestCalories(fileName):
  with open(fileName) as f:
    data = f.readlines()
    highest = -1
    curr = 0
    for line in data:
      if line != "\n":
        curr += int(line)
      else:
        highest = max(curr, highest)
        curr = 0
    return max(curr, highest)
    
if __name__ == "__main__":
  print(findHighestCalories("./input/1_input.txt"))