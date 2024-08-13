# Dynamic Programming, Greedy Algorithm

n = int(input())
seq = list(map(int, input().split()))
for i in range(1, n):
    if seq[i - 1] > 0:
        seq[i] += seq[i - 1]
print(max(seq))
