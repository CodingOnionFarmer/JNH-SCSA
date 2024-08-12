def judge(guess, answer):
    g1 = guess % 10
    g2 = guess // 10 % 10
    g3 = guess // 100 % 10
    a1 = answer % 10
    a2 = answer // 10 % 10
    a3 = answer // 100 % 10
    strike = 0
    not_strike = set()
    if a1 == g1:
        strike += 1
    else:
        not_strike.add(g1)
        not_strike.add(a1)
    if a2 == g2:
        strike += 1
    else:
        not_strike.add(g2)
        not_strike.add(a2)
    if a3 == g3:
        strike += 1
    else:
        not_strike.add(g3)
        not_strike.add(a3)
    return strike, 6 - strike * 2 - len(not_strike)


n = int(input())
candidates = []
for i in range(1, 10):
    for j in range(1, 10):
        if j == i:
            continue
        for k in range(1, 10):
            if k == i or k == j:
                continue
            candidates.append(i * 100 + j * 10 + k)
for i in range(n):
    result = list(map(int, input().split()))
    new_candidates = []
    for can in candidates:
        s, b = judge(result[0], can)
        if result[1] == s and result[2] == b:
            new_candidates.append(can)
    candidates = new_candidates
print(len(candidates))
