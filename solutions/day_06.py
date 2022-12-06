import sys

file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n')

def detector(data: list, size: int) -> list:
    pos = []
    for line in data:
        for i in range(len(line)):
            seq = line[i:i+size]
            if len(set(seq)) == len(seq):
                pos.append(i + size)
                break
    return pos

# 6.1
print(f'6.1: {detector(input, 4)[0]}')

# 6.2
print(f'6.2: {detector(input, 14)[0]}')