import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

m = int(input())
lines = []
while True:
    l, r = map(int, input().split())
    if not l and not r:
        break
    lines.append((l, r))
n = len(lines)
lines.sort()


def solve():
    end = 0
    idx = 0
    ans = 0
    while idx < n and end < m:
        new_end = end
        new_idx = idx
        while new_idx < n and lines[new_idx][0] <= end:
            if lines[new_idx][1] >= new_end:
                new_end = lines[new_idx][1]
            new_idx += 1
        if new_idx == idx or new_end == end:
            print(0)
            return
        end = new_end
        idx += 1
        ans += 1
    print(ans)
    return


solve()
