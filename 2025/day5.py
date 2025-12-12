# Run with: python day{#}.py {INPUT_PATH}, eg. python 2025/day5.py input/2025/day5.txt
import sys
data = (open(sys.argv[1], 'r')).readlines()
intervals = []
values = []
processIntervals = True
for line in data:
    if line == '\n':
        processIntervals = False
    else:
        if processIntervals:
            line = line.split('-')
            intervals.append([int(line[0]), int(line[1][:-1])])
        else:
            values.append(int(line[:-1]))

# Taken from https://github.com/chloecrozier/leetcode/blob/main/python/medium/0056_merge_intervals.py
intervals.sort()
start = intervals[0][0]
end = intervals[0][1]
merged = []
for interval in intervals:
    one = (interval[0] <= start and interval[1] >= start)
    two = (interval[1] >= end and interval[0] <= end)
    if (interval[0] <= start and interval[1] >= start) or (interval[1] >= end and interval[0] <= end) or (interval[0] >= start and interval[1] <= end):
        start = min(start, interval[0])
        end = max(end, interval[1])
    else:
        merged.append([start, end])
        start = interval[0]
        end = interval[1]
if not merged or (merged[-1][0] != start and merged[-1][1] != end):
    merged.append([start, end])

ans1 = 0
ans2 = 0
for val in values:
    for interval in merged:
        if val >= interval[0] and val <= interval[1]:
            ans1 += 1
            
for interval in merged:
    ans2 += interval[1] - interval[0] + 1

print('Part 1 Answer: ', ans1)
print('Part 2 Answer: ', ans2)