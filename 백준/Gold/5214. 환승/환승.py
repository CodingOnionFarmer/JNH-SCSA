n, k, m = map(int, input().split())
can_get_on = [set() for _ in range(n + 1)]
hyper_tubes = [set(map(int, input().split())) for _ in range(m)]
visited_tube = [False] * m
visited_station = [False] * (n + 1)

for idx, tube in enumerate(hyper_tubes):
    for station in tube:
        can_get_on[station].add(idx)
for tube_idx in can_get_on[1]:
    hyper_tubes[tube_idx].remove(1)

now = {1}
step = 1
visited_station[1] = True

while now and n not in now:
    move = set()
    for cs in now:
        for tube_idx in can_get_on[cs]:
            if visited_tube[tube_idx]:
                continue
            visited_tube[tube_idx] = True
            for station in hyper_tubes[tube_idx]:
                if visited_station[station]:
                    continue
                visited_station[station] = True
                move.add(station)
    now = move
    step += 1

if not now:
    print(-1)
else:
    print(step)
