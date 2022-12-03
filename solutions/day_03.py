import sys
import string

file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n')

# 3.1
## a-z = 1-26
## A-Z = 27-52
alphabet = string.ascii_lowercase + string.ascii_uppercase
sumPriority = 0
for i in input:
    half = len(i) // 2
    for letter in i[:half]:
        if letter in i[half:]:
            sumPriority += alphabet.find(letter) + 1
            break
print(f'3.1: {sumPriority}')

# 3.2
## groups of 3 (sets of 3 in input), find common item in 3 bags
# print (len(input))
n = 3
grouped = [input[i:i+n] for i in range(0,len(input), n)]
sumPriority = 0
for group in grouped:
    badge = set(group[0]) & set(group[1]) & set(group[2])
    sumPriority += alphabet.find(list(badge)[0]) + 1

print(f'3.2: {sumPriority}')
