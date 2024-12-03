def is_internal(x, y, cx, cy, r):
    dist = (x - cx) ** 2 + (y - cy) ** 2
    return dist < r ** 2


T = int(input())
for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        cnt += is_internal(x1, y1, cx, cy, r) ^ is_internal(x2, y2, cx, cy, r)
    print(cnt)
