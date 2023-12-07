import sys
from collections import defaultdict

data = open(sys.argv[1]).read().strip().split('\n')
RANK = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
hands = []
for line in data:
    hand = line.split()[0]
    bet = int(line.split()[1])
    seen = defaultdict(int)
    maxCount = 0
    for card in [*hand]:
        seen[card] += 1
        maxCount = max(maxCount, seen[card])
    if len(seen) == 1:
        hand_strength = 7
    elif len(seen) == 2 and maxCount == 4:
        hand_strength = 6
    elif len(seen) == 2 and maxCount == 3:
        hand_strength = 5
    elif len(seen) == 3 and maxCount == 3:
        hand_strength = 4
    elif len(seen) == 3 and maxCount == 2:
        hand_strength = 3
    elif len(seen) == 4 and maxCount == 2:
        hand_strength = 2
    else:
        hand_strength = 1
    hands.append((hand, hand_strength, bet))

sort1 = sorted(hands, key=lambda word: [RANK.index(c) for c in word[0]], reverse=True)
sort2 = sorted(sort1, key=lambda x: x[1])

p1 = 0
for i in range(len(sort2)):
    p1 += (i+1) * sort2[i][2]

print(p1)

# p2
# i dont have the brain capacity right now