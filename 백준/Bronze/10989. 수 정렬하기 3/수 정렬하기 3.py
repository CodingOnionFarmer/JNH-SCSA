import sys

input = sys.stdin.readline

n = int(input())
num_cnt = [0] * 10001
ans = ''
for _ in range(n):
    num_cnt[int(input())] += 1
for i in range(1, 10001):
    for j in range(num_cnt[i]):
        sys.stdout.write(str(i) + '\n')
