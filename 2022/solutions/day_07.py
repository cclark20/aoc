import sys
from collections import defaultdict

file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n')

# 7.1
fs = defaultdict(list)
cwd = ()
for cmd in input:
    if cmd.startswith('$'):
        if '$ cd ' in cmd:
            if "$ cd .." in cmd:
                cwd = cwd[:-1]
            else:
                new_cwd = cwd + (str(cmd[len("$ cd "):]),)
                fs[cwd].append(new_cwd)
                cwd = new_cwd
    else:
        size = cmd.split()[0]
        if size == 'dir':
            continue
        fs[cwd].append(int(size))
# print(fs)

def dir_size(fs, path, output=None):
    size = 0
    for i in fs[path]:
        if isinstance(i, int):
            size += i
        else:
            size += dir_size(fs, i, output)
    if output != None:
        output[path] = size
    return size

sizes = {}
dir_size(fs,('/',),sizes)
# print(sizes)
final = 0
for i in sizes.values():
    if i <= 100_000:
        final += i
print('7.1: ', final)

# 7.2
used = sizes[('/',)]
free = 70_000_000 - used
target = 30_000_000 - free

min_size_to_free = used

for path in fs: 
    size = dir_size(fs, path)
    if size >= target and size < min_size_to_free:
        min_size_to_free = size
print('7.2: ', min_size_to_free)