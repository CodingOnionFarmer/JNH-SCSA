import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
stack = []
biggest = 0
for i in range(n):
    h = int(input())
    idx = i
    while stack:
        if stack[-1][0] > h:
            height, idx = stack.pop()
            if height * (i - idx) > biggest:
                biggest = height * (i - idx)
        else:
            break
    stack.append((h, idx))
while stack:
    height, idx = stack.pop()
    biggest = max(biggest, height * (n - idx))
print(biggest)
