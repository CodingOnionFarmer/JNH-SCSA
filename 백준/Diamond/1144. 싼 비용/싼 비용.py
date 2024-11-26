n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]


def build(x):
    if x == 1:
        return [[0], [1]]
    li = build(x - 1)
    new_li = []
    for arr in li:
        t = max(arr)
        new_li.append(arr + [0])
        for i in range(1, t + 2):
            if not arr[-1] or arr[-1] == i:
                new_li.append(arr + [i])
    return new_li


def build_connection(x):
    for i in range(2 ** x):
        arr = []
        cnt = 1
        for j in range(x):
            if i % 2:
                arr.append(cnt)
            else:
                if arr and arr[-1]:
                    cnt += 1
                arr.append(0)
            i //= 2
        ma = max(arr)
        for before in connection:
            after = []
            numbered = [j for j in range(ma + 1)]
            con = {}
            for k in range(1, numbers[before] + 1):
                for j in nums_index[before][k]:
                    if arr[j]:
                        if before[j] in con:
                            numbered[arr[j]] = con[before[j]]
                        else:
                            con[before[j]] = numbered[arr[j]]
            if len(con) < numbers[before]:
                continue
            renumbered = sorted(list(set(numbered)))
            for j in range(ma + 1):
                numbered[j] = renumbered.index(numbered[j])
            for j in range(x):
                after.append(numbered[arr[j]])
            connection[tuple(after)].append(before)
    return


li = build(m)
connection = {tuple(arr): [] for arr in li}
numbers = {tu: max(tu) for tu in connection}
nums_index = {tu: [[] for _ in range(numbers[tu] + 1)] for tu in connection}
for tu in nums_index:
    for j in range(m):
        nums_index[tu][tu[j]].append(j)
build_connection(m)
scores = {tuple(arr): 100000 for arr in li}
for i in range(2 ** m):
    arr = []
    cnt = 1
    score = 0
    for j in range(m):
        if i % 2:
            arr.append(cnt)
            score += paper[0][j]
        else:
            if arr and arr[-1]:
                cnt += 1
            arr.append(0)
        i //= 2
    scores[tuple(arr)] = score
best = 0
for i in range(1, n):
    local_best = min(scores[tu] for tu in scores if max(tu) <= 1)
    if local_best < best:
        best = local_best
    new_scores = {}
    for new in scores:
        score = 0
        for j in range(m):
            if new[j]:
                score += paper[i][j]
        new_scores[new] = score + min(scores[old] for old in connection[new])
    scores = new_scores
local_best = min(scores[tu] for tu in scores if max(tu) <= 1)
if local_best < best:
    best = local_best
print(best)
