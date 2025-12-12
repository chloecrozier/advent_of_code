# Run with: python day{#}.py {INPUT_PATH}, eg. python 2025/day5.py input/2025/day5.txt
import sys
import re
data = (open(sys.argv[1], 'r')).readlines()

nums1 = []
for i in range(len(data) - 1):
    nums1.append(re.findall(r'\S+', data[i]))
operations = re.findall(r'\S+', data[-1])

ans1 = 0
curr = 0
calculated = []
for c in range(len(nums1[0])):
    if operations[c] == '+':
        curr = 0
    else:
        curr = 1
    for r in range(len(nums1)):
        if operations[c] == '+':
            curr += int(nums1[r][c])
        else:
            curr *= int(nums1[r][c])
    ans1 += curr

widths = []
width = data[-1][0]
for i in range(1, len(data[-1])):
    c = data[-1][i]
    if c == ' ':
        width += c
    else:
        widths.append(width)
        width = c
widths.append(width)

ans2 = 0
nums2 = []
for i in range(len(data) - 1):
    index = 0
    row = []
    for j in range(len(nums1[i])):
        width = len(widths[j]) - 1
        row.append(data[i][index:index + width])
        index += width + 1
    nums2.append(row)

groups = []
for c in range(len(nums2[0])):
    n = [''] * (len(widths[c]) - 1)
    for r in range(len(nums2)):
        for i in range(len(widths[c]) - 1):
            n[i] += nums2[r][c][i]
    groups.append([int(num.strip()) for num in n])

curr = 0
calculated = []
for i in range(len(groups)):
    if widths[i][0] == '+':
        curr = 0
        for j in range(len(groups[i])):
            curr += groups[i][j]
        ans2 += curr
    else:
        curr = 1
        for j in range(len(groups[i])):
            curr *= groups[i][j]
        ans2 += curr

print('Part 1 Answer: ', ans1)
print('Part 2 Answer: ', ans2)