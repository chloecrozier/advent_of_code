# Run with: python day{#}.py {INPUT_PATH}, eg. python 2025/day6.py input/2025/day6.txt
import sys
import re
data = (open(sys.argv[1], 'r')).readlines()

nums1 = []
for i in range(len(data) - 1):
    nums1.append(re.findall(r'\S+', data[i]))
operations = re.findall(r'\S+', data[-1])

ans1 = 0
ans2 = 0

print('Part 1 Answer: ', ans1)
print('Part 2 Answer: ', ans2)