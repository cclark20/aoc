import sys

data = open(sys.argv[1]).read().strip().split('\n')

times = data[0].split()[1:]
dists = data[1].split()[1:]

p1 = 1
for i in range(len(times)):
    time = int(times[i])
    dist = int(dists[i])
    winners = 0
    for j in range(time+1):
        mpms = j
        travel_time = time - j
        if mpms * travel_time > dist:
            winners += 1
    p1 *= winners

print(p1)

#p2
time = int(data[0].split(":")[1].replace(" ", ""))
dist = int(data[1].split(":")[1].replace(" ", ""))

first_idx = 0
for i in range(time+1):
    mpms = i
    travel_time = time - i
    if mpms * travel_time > dist:
        first_idx = i
        break
print( (time+1) - (first_idx*2) )