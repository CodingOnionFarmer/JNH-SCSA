n, m, g, r = map(int, input().split())
garden = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * m]
cultivable = []
for i in range(n):
    for j in range(m):
        if garden[i][j] == 2:
            cultivable.append((i, j))
c = len(cultivable)
cases = []
for case_code in range(3 ** c):
    green = []
    red = []
    idx = 0
    while case_code:
        code = case_code % 3
        if code == 1:
            green.append(cultivable[idx])
        elif code == 2:
            red.append(cultivable[idx])
        case_code //= 3
        idx += 1
    if len(green) == g and len(red) == r:
        cases.append([green, red])

most = 0
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
for case in cases:
    green = set(case[0])
    red = set(case[1])
    flower = 0
    visited = [[False] * m for _ in range(n)]
    while green and red:
        next_green = set()
        next_red = set()
        for ci, cj in green:
            visited[ci][cj] = True
        for ci, cj in red:
            visited[ci][cj] = True
        for ci, cj in green:
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if garden[ni][nj] and not visited[ni][nj]:
                    next_green.add((ni, nj))
        for ci, cj in red:
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if garden[ni][nj] and not visited[ni][nj]:
                    if (ni, nj) in next_green:
                        next_green.remove((ni, nj))
                        flower += 1
                        visited[ni][nj] = True
                    else:
                        next_red.add((ni, nj))
        green = next_green
        red = next_red
    if flower > most:
        most = flower


print(most)
