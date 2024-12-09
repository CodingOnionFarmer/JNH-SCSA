power = ((0, 2, 2, 2, 2), (0, 1, 3, 4, 3), (0, 3, 1, 3, 4), (0, 4, 3, 1, 3), (0, 3, 4, 3, 1))
order = list(map(int, input().split()))
now = {(0, 0): 0}
total = 0
for r in range(len(order) - 1):
    s = order[r]
    move = {}
    for a, b in now:
        c = now[a, b]
        if b != s:
            ac = c + power[a][s]
            if (s, b) not in move or ac < move[s, b]:
                move[s, b] = ac
        if a != s:
            bc = c + power[b][s]
            if (a, s) not in move or bc < move[a, s]:
                move[a, s] = bc
    now = move
print(min(now.values()))
