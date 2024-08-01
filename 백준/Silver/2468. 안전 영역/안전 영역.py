import sys

input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split())) + [0]
MIN = MAX = height[0]
for i in range(1, n):
    if MIN > height[i]:
        MIN = height[i]
    elif MAX < height[i]:
        MAX = height[i]
for _ in range(n - 1):
    for num in list(map(int, input().split())):
        if MIN > num:
            MIN = num
        elif MAX < num:
            MAX = num
        height.append(num)
    height.append(0)
for _ in range(n):
    height.append(0)

n += 1
ans = 1
not_sunken = {i for i in range(n * n - n) if (i + 1) % n and height[i] > MIN}
for rain in range(MIN, MAX):
    will_not_sink = set()
    island = 0
    while not_sunken:
        now = not_sunken.pop()
        if height[now] > rain + 1:
            will_not_sink.add(now)
        lands = [now]
        while lands:
            adj_land = []
            for land in lands:
                for adj in (land + 1, land - 1, land + n, land - n):
                    if adj in not_sunken:
                        adj_land.append(adj)
                        not_sunken.remove(adj)
                        if height[adj] > rain + 1:
                            will_not_sink.add(adj)
            lands = adj_land
        island += 1
    if island > ans:
        ans = island
    not_sunken = will_not_sink

print(ans)
