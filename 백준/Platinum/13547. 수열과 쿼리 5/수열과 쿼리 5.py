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
cnt = [0] * 1000001
start = 1
end = 1
cnt[sequence[1]] = 1
diff_numb = 1
for sect, j, i, q in queries:
    if j >= end:
        for idx in range(end + 1, j + 1):
            num = sequence[idx]
            if not cnt[num]:
                diff_numb += 1
            cnt[num] += 1
    else:
        for idx in range(j + 1, end + 1):
            num = sequence[idx]
            cnt[num] -= 1
            if not cnt[num]:
                diff_numb -= 1
    end = j
    if i <= start:
        for idx in range(i, start):
            num = sequence[idx]
            if not cnt[num]:
                diff_numb += 1
            cnt[num] += 1
    else:
        for idx in range(start, i):
            num = sequence[idx]
            cnt[num] -= 1
            if not cnt[num]:
                diff_numb -= 1
    start = i
    answer[q] = diff_numb

print(*answer, sep='\n')
