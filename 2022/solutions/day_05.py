import sys

file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n')


## 5.1
stacks = {}
instructions =[]
parseStacks = True
for i in input:
    if i == '':
        parseStacks=False
        continue
    blocks = [i[j:j+3] for j in range(0, len(i), 4)]
    if parseStacks:
        for j in range(len(blocks)):
            if '[' in blocks[j]:
                stacks.setdefault(j+1, []).append(blocks[j])
    else:
        instructions.append(i)

for key, value in stacks.items():
    stacks[key] = value[::-1]

for i in range(len(instructions)):
    iList = instructions[i].split(' ')
    n = int(iList[1])
    fromStack = stacks[int(iList[3])]
    toStack = stacks[int(iList[5])]
    for i in range(n):
        toStack.append(fromStack[-1])
        fromStack.pop()
    stacks[int(iList[3])] = fromStack
    stacks[int(iList[5])] = toStack

print(f"5.1: {''.join([stacks[i][-1][1] for i in sorted(stacks)])}")

## 5.2
stacks = {}
instructions =[]
parseStacks = True
for i in input:
    if i == '':
        parseStacks=False
        continue
    blocks = [i[j:j+3] for j in range(0, len(i), 4)]
    if parseStacks:
        for j in range(len(blocks)):
            if '[' in blocks[j]:
                stacks.setdefault(j+1, []).append(blocks[j])
    else:
        instructions.append(i)

for key, value in stacks.items():
    stacks[key] = value[::-1]

for i in range(len(instructions)):
    iList = instructions[i].split(' ')
    n = int(iList[1])
    fromStack = stacks[int(iList[3])]
    toStack = stacks[int(iList[5])]
    crates = fromStack[-n:]
    toStack.extend(crates)
    del fromStack[-n:]
    stacks[int(iList[3])] = fromStack
    stacks[int(iList[5])] = toStack

print(f"5.2: {''.join([stacks[i][-1][1] for i in sorted(stacks)])}")