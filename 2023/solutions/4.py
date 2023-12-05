import sys

data = open(sys.argv[1]).read().strip()

p1 = 0
p2 = 0
copy_list = [1] * len(data.split('\n'))
for i, line in enumerate(data.split('\n')):
    pts = 0
    matches = 0
    num_lists = line.split(': ')[1]
    winners = [int(num) for num in num_lists.split('|')[0].split()]
    guesses = [int(num) for num in num_lists.split('|')[1].split()]

    for guess in guesses:
        if guess in winners:
            if pts == 0:
                pts = 1
            else:
                pts *= 2

            matches += 1

    for _ in range(copy_list[i]):
        for j in range(i+1, i + matches + 1):
            copy_list[j] += 1
    

    p1 += pts
    p2 += copy_list[i]

print(p1)
print(p2)