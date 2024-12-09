def bs_acid(l, h, f):
    m = (l + h) // 2
    if l == m:
        global char
        if abs(acid2[h] - f) < abs(acid2[l] - f):
            if abs(acid2[h] - f) < char:
                char = abs(acid2[h] - f)
                return acid2[h]
            return 0
        if abs(acid2[l] - f) < char:
            char = abs(acid2[l] - f)
            return acid2[l]
        return 0
    if acid2[m] < f:
        return bs_acid(m, h, f)
    return bs_acid(l, m, f)


def bs_alk(l, h, f):
    m = (l + h) // 2
    if l == m:
        global char
        if abs(alk2[h] - f) < abs(alk2[l] - f):
            if abs(alk2[h] - f) < char:
                char = abs(alk2[h] - f)
                return alk2[h]
            return 0
        if abs(alk2[l] - f) < char:
            char = abs(alk2[l] - f)
            return alk2[l]
        return 0
    if alk2[m] < f:
        return bs_alk(m, h, f)
    return bs_alk(l, m, f)


n = int(input())
sols = list(map(int, input().split()))
alk = []
acid = []
for s in sols:
    if s < 0:
        alk.append(-s)
    else:
        acid.append(s)
alk.sort()
acid.sort()
best = (0, 0, 0)
char = 2 << 31
if len(alk) > 2:
    if alk[0] + alk[1] + alk[2] < char:
        char = alk[0] + alk[1] + alk[2]
        best = (-alk[2], -alk[1], -alk[0])
if len(acid) > 2:
    if acid[0] + acid[1] + acid[2] < char:
        char = acid[0] + acid[1] + acid[2]
        best = (acid[0], acid[1], acid[2])
alk2 = []
acid2 = []
for i in range(len(alk) - 1):
    for j in range(i + 1, len(alk)):
        alk2.append(alk[i] + alk[j])
for i in range(len(acid) - 1):
    for j in range(i + 1, len(acid)):
        acid2.append(acid[i] + acid[j])
alk2.sort()
acid2.sort()
if acid2:
    for i in range(len(alk)):
        find = alk[i]
        lo = 0
        hi = len(acid2) - 1
        s = bs_acid(lo, hi, find)
        if s:
            best = (-find, s)
if alk2:
    for i in range(len(acid)):
        find = acid[i]
        lo = 0
        hi = len(alk2) - 1
        s = bs_alk(lo, hi, find)
        if s:
            best = (find, s)
if len(best) == 2:
    found, check = best
    checked = False
    if found < 0:
        for i in range(len(acid) - 1):
            for j in range(i + 1, len(acid)):
                if acid[i] + acid[j] == check:
                    checked = True
                    best = (found, acid[i], acid[j])
                    break
            if checked:
                break
    else:
        for i in range(len(alk) - 1):
            for j in range(i + 1, len(alk)):
                if alk[i] + alk[j] == check:
                    checked = True
                    best = (-alk[j], -alk[i], found)
print(*best)
