n, m, g, r = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(n)]
connected = [[] for _ in range(n * m)]
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
for i in range(n):
    for j in range(m):
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                connected[i * m + j].append(ni * m + nj)
cultivable = []
original_visited = [False] * (m * n)
for i in range(n):
    for j in range(m):
        if garden[i][j] == 2:
            cultivable.append(i * m + j)
        elif not garden[i][j]:
            original_visited[i * m + j] = True

c = len(cultivable)
cases = []
for case_code in range(3 ** c):
    green = set()
    red = set()
    idx = 0
    while case_code:
        code = case_code % 3
        if code == 1:
            green.add(cultivable[idx])
        elif code == 2:
            red.add(cultivable[idx])
        case_code //= 3
        idx += 1
    if len(green) == g and len(red) == r:
        cases.append([green, red])

most = 0
for green, red in cases:
    flower = 0
    visited = original_visited[:]
    while green and red:
        next_green = set()
        next_red = set()
        for c in green:
            visited[c] = True
        for c in red:
            visited[c] = True
        for c in green:
            for adj in connected[c]:
                if not visited[adj]:
                    next_green.add(adj)
        for c in red:
            for adj in connected[c]:
                if not visited[adj]:
                    if adj in next_green:
                        next_green.remove(adj)
                        flower += 1
                        visited[adj] = True
                    else:
                        next_red.add(adj)
        green = next_green
        red = next_red
    if flower > most:
        most = flower

print(most)
