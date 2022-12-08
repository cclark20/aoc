import sys

file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n')

# 8.1
n = 0
for i, row in enumerate(input):
    for j, tree in enumerate(row):
        # get our edges
        if i == 0 or i == len(input)-1 or j == 0 or j == len(input[i])-1:
            n += 1
        # look around
        else:
            from_right  = (tree > t for t in row[j+1:])
            from_left   = (tree > t for t in row[:j])
            from_top    = (tree > input[t][j] for t in range(i-1, -1, -1))
            from_bottom = (tree > input[t][j] for t in range(i+1, len(input)))
            if all(from_right) or all(from_left) or all(from_top) or all(from_bottom):
                n += 1
print('8.1: ', n)

# 8.2
best = 0
for i, row in enumerate(input):
    for j, tree in enumerate(row):
        # remove our edges
        if i == 0 or i == len(input)-1 or j == 0 or j == len(input[i])-1:
            continue
        
        else:
            for right in range(j+1, len(row)):
                if row[right] >= tree:
                    break
            for left in range(j-1, -1, -1):
                if row[left] >= tree:
                    break
            for top in range(i-1, -1, -1):
                if input[top][j] >= tree:
                    break
            for bottom in range(i+1, len(input)):
                if input[bottom][j] >= tree:
                    break
        score = (right - j) * (j - left) * (bottom - i) * (i - top)
        if score > best:
            best = score

print('8.2: ', best)
            
