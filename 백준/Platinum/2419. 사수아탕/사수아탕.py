n, m = map(int, input().split())
basket = sorted([int(input()) for _ in range(n)])
ans = 0
cut = n
for i in range(n):
    if not basket[i]:
        cut = i
        basket.pop(i)
        ans += m
        n -= 1
        break
    if basket[i] > 0:
        cut = i
        break
left = basket[:cut] + [0]
left.reverse()
right = [0] + basket[cut:]
# for i in range(cut):
#     left.append()
# dp[i][j]는 왼쪽i개 오른쪽j개 먹었을때 (지난시간,사탕개수)의 튜플들의 집합
dpl = [[[] for _ in range(n - cut + 1)] for _ in range(cut + 1)]
dpr = [[[] for _ in range(n - cut + 1)] for _ in range(cut + 1)]
dpl[0][0].append((0, 0))
dpr[0][0].append((0, 0))
for i in range(1, cut + 1):
    for t, c in dpl[i - 1][0]:
        dpl[i][0].append((-left[i], c + max(0, m + left[i])))
for j in range(1, n - cut + 1):
    for t, c in dpr[0][j - 1]:
        dpr[0][j].append((right[j], c + max(0, m - right[j])))
for i in range(1, cut + 1):
    for j in range(1, n - cut + 1):
        dpl_temp = []
        dpr_temp = []
        for t, c in dpl[i - 1][j]:
            nt = t + left[i - 1] - left[i]
            dpl_temp.append((nt, c + max(0, m - nt)))
        for t, c in dpr[i - 1][j]:
            nt = t + right[j] - left[i]
            dpl_temp.append((nt, c + max(0, m - nt)))
        for t, c in dpl[i][j - 1]:
            nt = t + right[j] - left[i]
            dpr_temp.append((nt, c + max(0, m - nt)))
        for t, c in dpr[i][j - 1]:
            nt = t + right[j] - right[j - 1]
            dpr_temp.append((nt, c + max(0, m - nt)))
        dpl_temp.sort()
        dpr_temp.sort()
        now, best = 0, 0
        for t, c in dpl_temp:
            if t > now:
                if c > best:
                    dpl[i][j].append((t, c))
                    now = t
                    best = c
            else:
                if c > best:
                    if dpl[i][j]:
                        dpl[i][j].pop()
                    dpl[i][j].append((t, c))
                    best = c
        now, best = 0, 0
        for t, c in dpr_temp:
            if t > now:
                if c > best:
                    dpr[i][j].append((t, c))
                    now = t
                    best = c
            else:
                if c > best:
                    if dpr[i][j]:
                        dpr[i][j].pop()
                    dpr[i][j].append((t, c))
                    best = c

# print(left)
# print(right)
# pprint(dpr)
# pprint(dpl)
max_right = 0
max_left = 0
if dpr[cut][n-cut]:
    max_right = max(c for (t, c) in dpr[cut][n - cut])
if dpl[cut][n-cut]:
    max_left = max(c for (t, c) in dpl[cut][n - cut])
print(ans + max(max_left,max_right))
