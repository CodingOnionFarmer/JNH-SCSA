import sys

input = sys.stdin.readline

n = int(input())
numbers = [float(input()) for _ in range(n)]
ans = 0.0
now = 1
for i in range(n):
    now *= numbers[i]
    if now > ans:
        ans = now
    if now < 1:
        now = 1
print(f'{ans:.3f}')
