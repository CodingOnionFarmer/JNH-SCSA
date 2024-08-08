sy = [input() for _ in range(5)]
SY = [1 if sy[i][j] == 'Y' else 0 for i in range(5) for j in range(5)]
adj = [[] for _ in range(25)]
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
for i in range(5):
    for j in range(5):
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 5 and 0 <= nj < 5:
                adj[5 * i + j].append(5 * ni + nj)
visited = set()


def dfs(depth, princesses, head, y):
    if y == 4:
        return 0
    if depth == 7:
        return 1
    seven_princess = 0
    for i in range(head):
        sit = 1 << i
        if sit & princesses:
            continue
        for j in adj[i]:
            if (1 << j) & princesses:
                break
        else:
            continue
        one_more_princess = princesses | sit
        if one_more_princess not in visited:
            visited.add(one_more_princess)
            seven_princess += dfs(depth + 1, one_more_princess, head, y + SY[i])
    return seven_princess


ans = 0
for h in range(6, 25):
    visited.add(1 << h)
    ans += dfs(1, 1 << h, h, SY[h])

print(ans)
