fee = list(map(int, input().split()))
park_in, park_out = map(sorted, (zip(*[list(map(int, input().split())) for _ in range(3)])))
now = park_in[0]
ans = 0
trucks = 1
p1 = 1
p2 = 0
while p1 < 3:
    if park_in[p1] <= park_out[p2]:
        ans += (park_in[p1] - now) * fee[trucks - 1] * trucks
        now = park_in[p1]
        p1 += 1
        trucks += 1
    else:
        ans += (park_out[p2] - now) * fee[trucks - 1] * trucks
        now = park_out[p2]
        p2 += 1
        trucks -= 1
while p2 < 3:
    ans += (park_out[p2] - now) * fee[trucks - 1] * trucks
    now = park_out[p2]
    p2 += 1
    trucks -= 1

print(ans)
