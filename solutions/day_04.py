import sys

file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n')

# 4.1 - find number of pairs where one range fully contains the other
# 4.2 - find number of pairs with any overlap
input = [i.split(',') for i in input]

def genLists(pair):
    a = [i for i in range(int(pair[0].split('-')[0]),int(pair[0].split('-')[-1])+1, 1)]
    b = [i for i in range(int(pair[1].split('-')[0]),int(pair[1].split('-')[-1])+1, 1)]
    return a, b

countAll = 0
countAny = 0
for pair in input:
    a, b = genLists(pair)
    if all(i in b for i in a) or all(i in a for i in b):
        countAll += 1
    if any(i in b for i in a) or all(i in a for i in b):
        countAny += 1
print(f'4.1: {countAll}')
print(f'4.2: {countAny}')
