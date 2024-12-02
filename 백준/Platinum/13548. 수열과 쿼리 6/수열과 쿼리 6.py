import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
k = int(n ** 0.5)
sequence = [0] + list(map(int, input().split()))
m = int(input())
queries = []
answer = [0] * m
for q in range(m):
    i, j = map(int, input().split())
    sect = i // k
    queries.append((sect, j, i, q))  # sect, j 순으로 정렬
queries.sort()
cnt = [0] * 100001
cnt_cnt = [0] * 100001
start = 1
end = 1
cnt[sequence[1]] = 1
cnt_cnt[1] = 1
maximal_cc = 1
for sect, j, i, q in queries:
    if j >= end:
        for idx in range(end + 1, j + 1):
            num = sequence[idx]
            cnt[num] += 1
            c = cnt[num]
            if c > maximal_cc:
                maximal_cc = c
            cnt_cnt[c] += 1
            cnt_cnt[c-1] -= 1
    else:
        for idx in range(j + 1, end + 1):
            num = sequence[idx]
            c = cnt[num]
            cnt_cnt[c] -= 1
            cnt_cnt[c-1] += 1
            if c == maximal_cc and not cnt_cnt[c]:
                maximal_cc = c - 1
            cnt[num] -= 1
    end = j
    if i <= start:
        for idx in range(i, start):
            num = sequence[idx]
            cnt[num] += 1
            c = cnt[num]
            if c > maximal_cc:
                maximal_cc = c
            cnt_cnt[c] += 1
            cnt_cnt[c-1] -= 1
    else:
        for idx in range(start, i):
            num = sequence[idx]
            c = cnt[num]
            cnt_cnt[c] -= 1
            cnt_cnt[c-1] += 1
            if c == maximal_cc and not cnt_cnt[c]:
                maximal_cc = c - 1
            cnt[num] -= 1
    start = i
    answer[q] = maximal_cc

print(*answer, sep='\n')
