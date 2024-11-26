import math

n, p, v = map(int, input().split())
if n == 1:
    print(0)
else:
    d = 1
    time = n * p + v
    for i in range(int(math.log2(n)) + 1):
        d += 1
        m = int((n - 1) ** (1 / d))
        check = m ** d
        time_check = d * (m * p + v)
        # print(d, m)
        q = 0
        while check < n:
            check *= m + 1
            check //= m
            time_check += p
            q += 1
        # print(q, '만큼 증가')
        if time_check < time:
            time = time_check
    # print(d - 1)
    print(time)
