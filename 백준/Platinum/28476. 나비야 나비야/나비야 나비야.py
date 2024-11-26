import math

pi = math.pi

n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]
angles = [[] for _ in range(n)]
maximal = n * (n - 1) * (n - 2) * (n - 3) // 24
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        angle = math.atan2(dots[j][1] - dots[i][1], dots[j][0] - dots[i][0])
        angles[i].append(angle)
        if angle > 0:
            angles[j].append(angle - pi)
        else:
            angles[j].append(angle + pi)
# print(angles)
for i in range(n):
    angles[i].sort()
    # print(angles[i])
    cycle = angles[i] + angles[i]
    s = 0
    e = 1
    while s < n - 1:
        while e < n - 1:
            while cycle[e] - cycle[s] < pi and e < n - 1:
                # print(i, s, e, cycle[s], cycle[e])
                e += 1
            if e == n - 1:
                break
            m = max(0, e - s - 2)
            cnt += m * (m + 1) // 2
            # if e - s - 2 > 0:
            #     print(e - s - 2, i, s, e)
            s += 1
            if e == s:
                e += 1
        while cycle[e] - cycle[s] < -pi and s < n - 1:
            # print(i, s, e, cycle[s], cycle[e])
            e += 1
        m = max(0, e - s - 2)
        cnt += m * (m + 1) // 2
        # if e - s - 2 > 0:
        #     print(e - s - 2, i, s, e)
        s += 1
        if e == s:
            e += 1
print((cnt - 3 * maximal) * 2)
