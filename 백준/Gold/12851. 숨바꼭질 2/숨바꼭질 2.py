n, k = map(int, input().split())
if n >= k:
    print(n - k)
    print(1)
else:
    step = 0
    while k >= n << 1 and not k & 1:
        k >>= 1
        step += 1
    ceil = min(k * 2, 100001)
    visited = [0] * ceil
    min_step = [100001] * ceil
    now = {n}
    visited[n] = 1
    min_step[n] = step
    while not visited[k]:
        next_step = set()
        step += 1
        for position in now:
            for adj_position in (position - 1, position + 1, position << 1):
                if 0 <= adj_position < ceil and min_step[adj_position] >= step:
                    next_step.add(adj_position)
                    min_step[adj_position] = step
                    visited[adj_position] += visited[position]
        now = next_step
    print(step)
    print(visited[k])
