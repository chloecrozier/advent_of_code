# Run with: python day{#}.py {INPUT_PATH}, eg. python 2025/day3.py input/2025/day3.txt
import sys
data = (open(sys.argv[1], 'r')).readlines()

ans1 = 0
ans2 = 0
NUM_BATTERIES = 12
for bank in data:
    bank = bank.strip()
    maxVal = max(bank)
    maxIndex = bank.index(maxVal)
    
    if maxIndex == (len(bank) - 1):
        ans1 += (int(max(bank[0:-1])) * 10) + int(maxVal)
    else:
        ans1 += (int(maxVal) * 10) + int(max(bank[maxIndex + 1:]))



    leftMax = max(bank[:(len(bank) - 12)])
    leftMaxIndex = bank.index(leftMax)
    bank = bank[leftMaxIndex:]
    curr = 0
    while len(bank) > NUM_BATTERIES:
        if curr + 1 < len(bank):
            if bank[curr] < bank[curr + 1]:
                bank = bank[0:curr] + bank[curr + 1:]
                curr -= 1
            else:
                curr += 1
        else:
            bank = bank[:NUM_BATTERIES]

    ans2 += int(bank)

print('Part 1 Answer: ', ans1)
print('Part 2 Answer: ', ans2)
print('')