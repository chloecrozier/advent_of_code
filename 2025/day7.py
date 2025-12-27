# Run with: python day{#}.py {INPUT_PATH}, eg. python 2025/day7.py input/2025/day7.txt
import sys
import re
data = (open(sys.argv[1], 'r')).readlines()
beams = [0] * len(data[0])
beams[data[0].index('S')] = 1

print(beams)

for i in range(1, len(data)):
    splitters = data[i].count('^')
    for j in range data[i].count('^'):
        if beams[data[i].index()]
    print(i)
# nums1 = []
# for i in range(len(data) - 1):
#     nums1.append(re.findall(r'\S+', data[i]))
# operations = re.findall(r'\S+', data[-1])



ans1 = 0
ans2 = 0

print('Part 1 Answer: ', ans1)
print('Part 2 Answer: ', ans2)