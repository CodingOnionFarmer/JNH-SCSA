def service():
    for size in range(max_size, 1, -1):
        cost = size * size + (size - 1) * (size - 1)
        maximal_houses = 0
        cp = min((size - 1) >> 1, (n - 1) >> 1)
        for cx in range(cp, n - cp):
            for cy in range(cp, n - cp):
                cnt = 0
                for x in range(max(0, cx - size + 1), min(n, cx + size)):
                    dx = abs(cx - x)
                    for y in range(max(0, cy - size + 1 + dx), min(n, cy + size - dx)):
                        cnt += city[x][y]
                if cnt * m >= cost:
                    maximal_houses = max(maximal_houses, cnt)
        if maximal_houses:
            return maximal_houses
    return 1


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    total = sum(sum(line) for line in city) * m
    max_size = 1
    while max_size * max_size + (max_size + 1) * (max_size + 1) <= total:
        max_size += 1
    print(f'#{tc}', service())
