# Run with: python day{#}.py {INPUT_PATH}, eg. python 2025/day1.py input/2025/day2.txt
import sys
import regex
data = ''
with open(sys.argv[1],'r') as f:
    data = f.read()
data = data.split(',')

ans1 = 0
ans2 = 0
for numRange in data:
    numRange = numRange.split('-')
    for i in range(int(numRange[0]), int(numRange[1]) + 1):
        currLength = len(str(i))
        if currLength % 2 == 0:
            if str(i)[:(currLength // 2)] == str(i)[(currLength // 2):]:
                ans1 += i

        for j in range(1, (currLength // 2) + 1):
            if (currLength // j) == (currLength / j):
                if str(i).count(str(i)[:j]) == currLength // j:
                    ans2 += i
                    break

print('Part 1 Answer: ', ans1)
print('Part 2 Answer: ', ans2)
print('')