import sys

n = int(input())
sols = list(map(int, sys.stdin.readline().split()))
alkali = []
acid = []
for sol in sols:
    if sol > 0:
        acid.append(sol)
    else:
        alkali.append(-sol)
acid.sort()
alkali.sort()
min_c = 2000000000
best = [0, 0]
if len(acid) > 1:
    min_c = acid[0] + acid[1]
    best = [acid[0], acid[1]]
if len(alkali) > 1 and alkali[0] + alkali[1] < min_c:
    min_c = alkali[0] + alkali[1]
    best = [-alkali[1], -alkali[0]]


def bs_alkali(c, s, e):
    if e - s == 1:
        global min_c
        if abs(alkali[s] - c) < min_c:
            min_c = abs(alkali[s] - c)
            best[0], best[1] = -alkali[s], c
        if abs(alkali[e] - c) < min_c:
            min_c = abs(alkali[e] - c)
            best[0], best[1] = -alkali[e], c
        return
    m = (s + e) // 2
    if alkali[m] == c:
        min_c = 0
        best[0], best[1] = -c, c
        return
    if alkali[m] > c:
        bs_alkali(c, s, m)
    else:
        bs_alkali(c, m, e)
    return


def bs_acid(c, s, e):
    if e - s < 2:
        global min_c
        if abs(acid[s] - c) < min_c:
            min_c = abs(acid[s] - c)
            best[0], best[1] = -c, acid[s]
        if abs(acid[e] - c) < min_c:
            min_c = abs(acid[e] - c)
            best[0], best[1] = -c, -acid[e]
        return
    m = (s + e) // 2
    if acid[m] == c:
        min_c = 0
        best[0], best[1] = -c, c
        return
    if acid[m] > c:
        bs_acid(c, s, m)
    else:
        bs_acid(c, m, e)
    return


if alkali:
    for c in acid:
        if min_c:
            bs_alkali(c, 0, len(alkali) - 1)
        else:
            break
if acid:
    for c in alkali:
        if min_c:
            bs_acid(c, 0, len(acid) - 1)
        else:
            break
print(*best)
