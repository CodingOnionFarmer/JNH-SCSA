import sys

n = int(input())
x, y = map(int, input().split())
x1, y1 = x, y
s1 = s2 = 0

for i in range(n - 1):
    x2, y2 = map(int, sys.stdin.readline().split())
    s1 += x1 * y2
    s2 += y1 * x2
    x1, y1 = x2, y2

s1 += x1 * y
s2 += y1 * x
print(abs(s1 - s2) / 2)
