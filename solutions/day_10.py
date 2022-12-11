import sys

file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n')

# 10.1
x = 1
iterator = 0
piterator = 0
check = 0
signals = []
line=[]
print('10.2: ')
for cyc in range(1, 240+1):
    # drawings
    if len(line) in [x-1,x,x+1]:
        line.append('#')
    else:
        line.append('.')

    # print line
    if len(line)==40:
        print(''.join(i for i in line))
        line = []

    if cyc in [i for i in range(20,250,40)]:
        signals.append(cyc*x)

    if input[iterator] == 'noop':
        iterator+=1
        continue
    else:
        if check == 1:
            x += int(input[iterator].split()[-1])
            iterator += 1
            check = 0 
        else:
            check += 1

print('\n10.1' ,sum(signals))


'''
if addx, dont do anything first time
second time, update x and increase iterator
how will it know when it's the second time seeing it

on first pass, iterator will be a new number from the last loop
if iterator didn't change, then must be the second time

'''