import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
seq = [int(input()) for _ in range(n)]
stack = []
ops = []
now = 1
cannot_make = False
for num in seq:
    while num >= now:
        stack.append(now)
        ops.append('+')
        now += 1
    if stack[-1] != num:
        cannot_make = True
        break
    stack.pop()
    ops.append('-')
if cannot_make:
    print('NO')
else:
    for op in ops:
        print(op + '\n')
