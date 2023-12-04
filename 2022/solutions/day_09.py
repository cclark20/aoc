import sys

file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n')

# 9.1
hx, hy = 0, 0
hpx, hpy = 0, 0
tx, ty = 0, 0
seen = [(0,0)]

for i in range(len(input)):
    dir, n = input[i].split()
    n = int(n)
    for j in range(n):
        if dir == "U":
            hy += 1
        elif dir == "D":
            hy -= 1
        elif dir == "R":
            hx += 1
        elif dir == "L":
            hx -= 1
        
        if abs(hx - tx) >= 2 or abs(hy - ty) >= 2:
            tx, ty = hpx, hpy
        if (tx, ty) not in seen:
            seen.append((tx, ty))
        hpx, hpy = hx, hy
        # print(f'head: {hx}, {hy} | tail: {tx}, {ty}')

print('9.1: ', len(seen))

# 9.2

## Surely there's a better way to do this part
hx, hy = 0, 0
ax, ay = 0, 0
bx, by = 0, 0
cx, cy = 0, 0
dx, dy = 0, 0
ex, ey = 0, 0
fx, fy = 0, 0
gx, gy = 0, 0
ix, iy = 0, 0
tx, ty = 0, 0
seen = [(0,0)]

def check(hx, hy, tx, ty, seen=None):
    if abs(hx - tx) >= 2 or abs(hy - ty) >= 2:
        if hx == tx:
            if hy > ty:
                ty += 1
            else:
                ty -= 1
        elif hy == ty:
            if hx > tx:
                tx += 1
            else:
                tx -= 1
        else:
            if hx > tx:
                    tx+=1
            else:
                tx-=1
            if hy > ty:
                ty+=1
            else:
                ty-=1
            
    if seen:
        if (tx, ty) not in seen:
            seen.append((tx, ty))
        return tx, ty, seen
    return tx, ty

    

for i in range(len(input)):
    dir, n = input[i].split()
    n = int(n)
    for j in range(n):
        if dir == "U":
            hy += 1
        elif dir == "D":
            hy -= 1
        elif dir == "R":
            hx += 1
        elif dir == "L":
            hx -= 1

        ax, ay = check(hx, hy, ax, ay)
        bx, by = check(ax, ay, bx, by)
        cx, cy = check(bx, by, cx, cy)
        dx, dy = check(cx, cy, dx, dy)
        ex, ey = check(dx, dy, ex, ey)
        fx, fy = check(ex, ey, fx, fy)
        gx, gy = check(fx, fy, gx, gy)
        ix, iy = check(gx, gy, ix, iy)
        tx, ty, seen = check(ix, iy, tx, ty, seen)


print('9.2: ', len(seen))