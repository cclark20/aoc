import sys

# 1.1
file = str(sys.argv[1:][0]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n\n')

elves = [list(map(int, elf.split())) for elf in input]
sums = [sum(elf) for elf in elves]
top = max(sums)
print(f'Part 1: {top:,}')

# 1.2
top3 = sorted(sums)[-3:]
print(f'top 3: {top3}')
print(f'Part 2: {sum(top3):,}')