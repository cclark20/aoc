import sys
file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read()

# 2.1
## A/X: Rock, 1 pt
## B/Y: Paper, 2 pt
## C/Z: Scissors, 3 pt
## lose: 0 pt
## draw: 3 pt
## win: 6 pt
pairs = [i.split() for i in input.split('\n')]
score = 0
for pair in pairs:
    if pair[1] == 'X':
        if pair[0] == 'A':
            score += 1+3
        elif pair[0] == 'B':
            score += 1+0
        elif pair[0] == 'C':
            score += 1+6
    elif pair[1] == 'Y':
        if pair[0] == 'A':
            score += 2+6
        elif pair[0] == 'B':
            score += 2+3
        elif pair[0] == 'C':
            score += 2+0
    elif pair[1] == 'Z':
        if pair[0] == 'A':
            score += 3+0
        elif pair[0] == 'B':
            score += 3+6
        elif pair[0] == 'C':
            score += 3+3
print(f'2.1: {score}')

# 2.2
## A: Rock, 1 pt
## B: Paper, 2 pt
## C: Scissors, 3 pt
## X: lose, 0 pt
## Y: draw, 3 pt
## Z: win, 6 pt
score = 0
for pair in pairs:
    if pair[1] == 'X': # lose
        if pair[0] == 'A':
            score += 0+3
        elif pair[0] == 'B':
            score += 0+1
        elif pair[0] == 'C':
            score += 0+2
    if pair[1] == 'Y': # draw
        if pair[0] == 'A':
            score += 3+1
        elif pair[0] == 'B':
            score += 3+2
        elif pair[0] == 'C':
            score += 3+3
    if pair[1] == 'Z': # win
        if pair[0] == 'A':
            score += 6+2
        elif pair[0] == 'B':
            score += 6+3
        elif pair[0] == 'C':
            score += 6+1
print(f'2.2: {score}')