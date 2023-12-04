import sys

file = str(sys.argv[1]) # file passed through command line
with open(file) as f:
    input = f.read().split('\n\n')

# 11
class Monkey():
    __slots__ = (
        'number', 'items', 'op', 'op_value', 'divisor',
        'pass_true', 'pass_false', 'inspections'
    )

    def inspect(self):
        item = self.items.popleft()
        if self.op == '+':
            return ( item + self.op_value ) // 3
        if self.op == '*':
            return ( item * self.op_value ) // 3
    
    def test(self):
        op_item = self.inspect()
        if op_item % self.divisor == 0:
            monkeys[m.pass_true].items.append()
        else:
            monkeys[m.pass_false].items.append()


monkeys = []
for i in range(len(input)):
    lines = input[i].split('\n')
    
    m = Monkey()
    m.number      = lines[0].split()[1][:-1]
    m.items       = [int(item.strip()) for item in lines[1][18:].split(',')]
    m.op          = lines[2][23:].split()[0]
    m.op_value    = lines[2][23:].split()[1]
    m.divisor     = lines[3].split()[-1]
    m.pass_true   = lines[4].split()[-1]
    m.pass_false  = lines[5].split()[-1]
    m.inspections = 0
    monkeys.append(m)

for i in range(20):
    


