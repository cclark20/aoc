import sys
import math

data = open(sys.argv[1]).read().strip()

seeds = [int(num) for num in data.split('\n')[0].split(': ')[1].split()]
mappings = data.split('\n\n')[1:]

p1 = math.inf
p2 = math.inf
for i, seed in enumerate(seeds):
    num = seed
    for mapping in mappings:
        mapping = [[int(x) for x in m.split()] for m in mapping.split(':')[1].split('\n')[1:]]
        for m in mapping:
            if m[1] <= num <= (m[1] + m[2] - 1):
                conv = m[0]- m[1]
                num = num + conv
                break
    p1 = min(p1, num)

    # if i%2 != 0:
    #     continue
    # num = seed
    # for mapping in mappings:
    #     mapping = [[int(x) for x in m.split()] for m in mapping.split(':')[1].split('\n')[1:]]
    #     for m in mapping:
    #         if m[1] <= num <= (m[1] + m[2] - 1):
    #             conv = m[0]- m[1]
    #             num = num + conv
    #             break
    # p2 = min(p2, num)

print(p1)
print(p2)

#p2
# for i in range(0, len(seeds), 2):
#     print(f'seed: {seeds[i]}')
#     print(f'reps: {seeds[i+1]}')
#     print()


# more_seeds = []
# i = 0
# while i < len(seeds):
#     more_seeds.extend(list(range(seeds[i], seeds[i]+seeds[i+1])))
#     i += 2

# print(len(more_seeds))

# p2 = math.inf
# for seed in more_seeds:
#     num = seed
#     for mapping in mappings:
#         mapping = [[int(x) for x in m.split()] for m in mapping.split(':')[1].split('\n')[1:]]
#         for m in mapping:
#             if m[1] <= num <= (m[1] + m[2] - 1):
#                 conv = m[0]- m[1]
#                 num = num + conv
#                 break
#     p2 = min(p2, num)
# print(p2)