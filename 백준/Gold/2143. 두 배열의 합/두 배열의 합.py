t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))
subA = {}
for i in range(n):
    s = 0
    for j in range(i, n):
        s += A[j]
        if s in subA:
            subA[s] += 1
        else:
            subA[s] = 1
subB = {}
for i in range(m):
    s = 0
    for j in range(i, m):
        s += B[j]
        if s in subB:
            subB[s] += 1
        else:
            subB[s] = 1
sortedB = sorted(subB.keys())
cnt = 0
for a in subA:
    find = t - a
    lo = 0
    hi = len(sortedB) - 1
    mid = (lo + hi) // 2
    while lo < mid and sortedB[mid] != find:
        if sortedB[mid] < find:
            lo = mid
            mid = (lo + hi) // 2
        else:
            hi = mid
            mid = (lo + hi) // 2
    if sortedB[mid] == find or sortedB[hi] == find:
        cnt += subA[a] * subB[find]
print(cnt)
