# Run with: python day{#}.py {INPUT_PATH}, eg. python 2025/day5.py input/2025/day5.txt
import sys
data = (open(sys.argv[1], 'r')).readlines()

presentData = data[:30]
shapes = [[''] * 3 for _ in range(6)] # each present has an area of 7 units
num = 0
for i in range(len(presentData)):
    if len(presentData[i]) > 2 and presentData[i][1] == ':':
        shapes[num][0] += presentData[i + 1][:-1]
        shapes[num][1] += presentData[i + 2][:-1]
        shapes[num][2] += presentData[i + 3][:-1]
        num += 1
    
regionData = data[30:]
regions = []
for region in regionData:
    counts = region[:-1].split(' ')[1:]
    counts = [int(n) for n in counts]
    dimensions = (region[:-1].split(' ')[0]).split('x')
    regions.append([[int(dimensions[0]), int(dimensions[1][:-1])], counts])

print(shapes)
print(regions)
    

ans1 = 0
ans2 = 0


# print('Part 1 Answer: ', ans1)
# print('Part 2 Answer: ', ans2)