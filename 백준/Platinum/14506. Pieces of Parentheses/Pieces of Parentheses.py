n = int(input())
pieces = [input() for _ in range(n)]


def check(p):
    left_max = 0
    is_left = True
    now = 0  # ( -1, ) +1
    for i in range(len(p)):
        if p[i] == '(':
            now -= 1
        else:
            now += 1
            if now > left_max:
                left_max += 1
    if now > 0:
        is_left = False
    if is_left:
        return True, left_max, -now
    right_max = 0
    now = 0
    for i in range(len(p) - 1, -1, -1):
        if p[i] == ')':
            now -= 1
        else:
            now += 1
            if now > right_max:
                right_max += 1
    return False, right_max, -now


left = []
right = []
for i in range(n):
    L, cut, weight = check(pieces[i])
    if L:
        left.append((cut, weight, len(pieces[i])))
    else:
        right.append((cut, weight, len(pieces[i])))
left.sort()
right.sort()
ksl = [0] * 90001  # knapsack of left
left_maximal = 0
for i in range(len(left)):
    c, w, v = left[i]  # cut, weight, value
    p = left_maximal
    if c > p:
        break
    left_maximal += w
    while p >= c:
        if ksl[p] >= p:
            ksl[p + w] = max(ksl[p + w], ksl[p] + v)
        p -= 1
ksr = [0] * 90001  # knapsack of right
right_maximal = 0
for i in range(len(right)):
    c, w, v = right[i]  # cut, weight, value
    p = right_maximal
    if c > p:
        break
    right_maximal += w
    while p >= c:
        if ksr[p] >= p:
            ksr[p + w] = max(ksr[p + w], ksr[p] + v)
        p -= 1

print(max(ksl[i] + ksr[i] for i in range(0, min(left_maximal, right_maximal) + 1) if ksl[i] >= i and ksr[i] >= i))
