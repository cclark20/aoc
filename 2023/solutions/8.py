import sys
import ast

data = open(sys.argv[1]).read().strip()

L_R = data.split('\n\n')[0]
M = {}
for line in data.split('\n\n')[1].split('\n'):
    key = line.split(' = ')[0]
    options = line.split(' = ')[1][1:-1].split(', ')
    val = (options[0], options[1])
    
    M[key] = val

curr = 'AAA'
dest = 'ZZZ'
L_R_idx = 0
p1 = 0
while curr != dest:
    if L_R_idx >= len(L_R):
        L_R_idx = 0
    options = M[curr]

    direction = L_R[L_R_idx]
    if direction == 'L':
        curr = options[0]
    else:
        curr = options[1]
    p1 += 1
    L_R_idx += 1

print(p1)


#############################################################################
## I could not figure this one out. the solution below was taken from:
## https://github.com/jonathanpaulson/AdventOfCode/blob/master/2023/8.py
## I brought it in just to understand how to do it.
## my brute force method wouldve taken farrrrrrrrrrrrrrrr too long if it ever even completed.
## its also below the following solution
#############################################################################

from math import gcd

def lcm(xs):
  ans = 1
  for x in xs:
    ans = (x*ans)//gcd(x,ans)
  return ans

GO = {'L': {}, 'R': {}}
steps, rule = data.split('\n\n')
for line in rule.split('\n'):
    st, lr = line.split('=')
    st = st.strip()
    left,right = lr.split(',')
    left = left.strip()[1:].strip()
    right = right[:-1].strip()
    GO['L'][st] = left
    GO['R'][st] = right


POS = []
for s in GO['L']:
    if s.endswith('A'):
        POS.append(s)

print(POS)
T = {}
t = 0
while True:
    NP = []
    for i,p in enumerate(POS):
        # get remainder of t / len(steps) to get current direction
        # use direction to get correct maps from GO dict, then get current vals next spot
        p = GO[steps[ t % len(steps)]][p]
        if p.endswith('Z'):
            # each index of starters will have the value of the number of loops it took to get here, +1
            T[i] = t+1
            print(T)
            # one each starter as found a z, length of T will match POS and we can calculate how many steps
            # doesnt mean they all currently are at Z
            if len(T) == len(POS):
                print('hit')
                print(lcm(T.values()))
                exit()
        # if new loc doesnt end in Z, add the loc to a list to keep track of current location
        NP.append(p)
    # update our locations and loop counter
    POS = NP
    t += 1




#p2
# currs = [node for node in list(M.keys()) if node.endswith('A')]
# print(currs)

# L_R_idx = 0
# p2 = 0
# done = False
# while done == False:
#     if L_R_idx >= len(L_R):
#         L_R_idx = 0

#     for i, curr in enumerate(currs):
#         options = M[curr]

#         direction = L_R[L_R_idx]
#         if direction == 'L':
#             currs[i] = options[0]
#         else:
#             currs[i] = options[1]
        
#     p2 += 1
#     L_R_idx += 1

#     if all([curr.endswith('Z') for curr in currs]):
#         print(currs)
#         done = True

# print(p2)