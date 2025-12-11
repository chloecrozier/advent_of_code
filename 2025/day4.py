# Run with: python day{#}.py {INPUT_PATH}, eg. python 2025/day4.py input/2025/day4.txt
import sys
import copy
data = (open(sys.argv[1], 'r')).readlines()

for r in range(len(data)):
    data[r] = list(data[r])
    data[r] = data[r][:-1]
    data[r] = ['0'] + data[r] + ['0']
data = (['0' * len(data[0])]) + data + (['0' * len(data[0])])

ans1 = 0
for r in range(1, len(data) - 1):
    for c in range(1, len(data[r]) - 1):
        count = 0
        if data[r][c] == '@':
            if data[r - 1][c - 1] == '@':
                count += 1
            if data[r - 1][c] == '@':
                count += 1
            if data[r - 1][c + 1] == '@':
                count += 1

            if data[r][c - 1] == '@':
                count += 1
            if data[r][c + 1] == '@':
                count += 1
            
            if data[r + 1][c - 1] == '@':
                count += 1
            if data[r + 1][c] == '@':
                count += 1
            if data[r + 1][c + 1] == '@':
                count += 1

            if count < 4:
                ans1 += 1

ans2 = 0
lastCount = 0
canContinue = True
while canContinue:
    temp = copy.deepcopy(data)
    for r in range(1, len(data) - 1):
        for c in range(1, len(data[r]) - 1):
            count = 0
            if data[r][c] == '@':
                if data[r - 1][c - 1] == '@':
                    count += 1
                if data[r - 1][c] == '@':
                    count += 1
                if data[r - 1][c + 1] == '@':
                    count += 1

                if data[r][c - 1] == '@':
                    count += 1
                if data[r][c + 1] == '@':
                    count += 1
                
                if data[r + 1][c - 1] == '@':
                    count += 1
                if data[r + 1][c] == '@':
                    count += 1
                if data[r + 1][c + 1] == '@':
                    count += 1

                if count < 4:
                    temp[r][c] = 'X'
                    ans2 += 1

    data = temp
    if ans2 > lastCount:
        lastCount = ans2
    else:
        canContinue = False

print('Part 1 Answer: ', ans1)
print('Part 2 Answer: ', ans2)