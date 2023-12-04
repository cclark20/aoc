import sys

data = open(sys.argv[1]).read().strip()

def valid(rnds:list):
    for rnd in rnds:
        for amt in rnd:
            if amt.split()[1] == "red":
                if int(amt.split()[0]) > 12:
                    return False
            elif amt.split()[1] == "green":
                if int(amt.split()[0]) > 13:
                    return False
            elif amt.split()[1] == "blue":
                if int(amt.split()[0]) > 14:
                    return False
    return True

possible_ids = []
powers = []
for line in data.split('\n'):
    
    game_id = int(line.split(": ")[0].split()[-1])
    game = line.split(": ")[1]
    rnds = [rnd.split(', ') for rnd in game.split("; ")]
    if valid(rnds):
        possible_ids.append(game_id)

    red = 0
    green = 0
    blue = 0
    for rnd in rnds:

        for amt in rnd:
            if amt.split()[1] == "red":
                red = max(red, int(amt.split()[0]))
            if amt.split()[1] == "green":
                green = max(green, int(amt.split()[0]))
            if amt.split()[1] == "blue":
                blue = max(blue, int(amt.split()[0]))

    powers.append(red * green * blue)
        
print(sum(possible_ids))
print(sum(powers))

