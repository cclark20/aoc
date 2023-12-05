import sys

data = open(sys.argv[1]).read().strip()
G = [line for line in data.split('\n')]
R = len(G)
C = len(G[0])

p1 = 0
for r in range(len(G)):
    n = 0
    has_part = False
    for c in range(len(G[r])+1):
        if c<C and G[r][c].isnumeric():
            n = n*10 + int(G[r][c])
            for rr in [-1,0,1]:
                for cc in [-1,0,1]:
                    if 0<=r+rr<R and 0<=c+cc<C:
                        ch = G[r+rr][c+cc]
                        if not ch.isnumeric() and ch != '.':
                            has_part=True
        elif n > 0:
            if has_part:
                p1 += n
            n = 0
            has_part = False




print(p1)









    # j = 0
    # while j < len(line):
    # # for j, char in enumerate(line):
    #     # print(j)
    #     char = line[j]
    #     if char.isnumeric():
    #         for k in range(j, len(line)):
    #             if not line[k].isnumeric():
    #                 part_no = line[j:k]
    #                 print(f'{line[j:k]} at {i}, {j}-{k}')
    #                 if i != 0 or i != len(schema) - 1:
    #                     neighbors = schema[i-1][j-1:k+1] + schema[i][j-1] + schema[i][k+1] + schema[i+1][j-1:k+1]
    #                     # neighbors = schema[i+1][j-1:k+1]
    #                     print(neighbors)



    #                 j = k
    #                 break
            
    #     else:
    #         j += 1
        
        
        

        # if not char.isnumeric() and not char == '.':
        #     print(f'{char} at {i},{j}')
        #     # top left
        #     if schema[i-1][j-1].isnumeric():
        #         print('yes')
        #     if schema[i-1][j].isnumeric():
        #         print()
        #     if schema[i+1][j-1].isnumeric():
            