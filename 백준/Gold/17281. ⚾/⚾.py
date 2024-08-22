n = int(input())
results = [list(map(int, input().split())) for _ in range(n)]
batter = [0] * 9
base = [0, 0, 0]
best = 0
memo = [0] * (1 << 9)


def dfs(depth, occupied):
    # print(depth)
    if depth == 9:
        game()
        return
    for i in range(1, 9):
        if (1 << i) & occupied:
            continue
        batter[depth] = i
        if depth != 2:
            dfs(depth + 1, occupied | (1 << i))
        else:
            dfs(depth + 2, occupied | (1 << i))


def game():
    score = 0
    now = 0
    for turn in range(n):
        base[0] = base[1] = base[2] = 0
        out = 0
        hit = []
        while out < 3:
            cb = batter[now]
            r = results[turn][cb]
            if not r:
                out += 1
            else:
                hit.append(r)
            now = (now + 1) % 9
        if hit:
            not_back_home = 0
            hit_sum = 0
            while not_back_home < len(hit):
                hit_sum += hit[-1 - not_back_home]
                if hit_sum < 4:
                    not_back_home += 1
                    continue
                break
            score += len(hit) - not_back_home
    global best
    if score > best:
        best = score


dfs(0, 1)
print(best)
