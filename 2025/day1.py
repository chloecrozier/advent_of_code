# Run with: python day{#}.py {INPUT_PATH}, eg. python 2025/day1.py input/2025/day1.txt
import sys
data = (open(sys.argv[1], 'r')).readlines()

MAX_VAL = 99
START_VAL = 50
MIN_VAL = 0

ans1 = 0
ans2 = 0
currLoc = START_VAL
for move in data:
    nextLoc = MIN_VAL
    turns = int(move[1:-1])
    
    if move[0] == 'R':
        nextLoc = currLoc + (turns % (MAX_VAL + 1))
        ans2 += turns // (MAX_VAL + 1)
        if nextLoc > MAX_VAL:
            nextLoc = (nextLoc % MAX_VAL) - 1
            if nextLoc != 0:
                ans2 += 1
                # print("\tOVER THRESHOLD")

    else:
        nextLoc = currLoc - (turns % (MAX_VAL + 1))
        ans2 += turns // (MAX_VAL + 1)
        if nextLoc < MIN_VAL:
            nextLoc += (MAX_VAL + 1)
            if currLoc != 0:
                ans2 += 1
                # print("\tUNDER THRESHOLD")

    print(currLoc, ' goes to ', nextLoc, ' after ', move[:-1])
    
    currLoc = nextLoc
    if currLoc == 0:
        ans1 += 1
        ans2 += 1

    print('Part 1 Answer: ', ans1)
    print('Part 2 Answer: ', ans2)
    print('')