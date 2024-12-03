import sys, math

input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    # n, m = max(n, m), min(n, m)
    if n >= m:
        if n % 2:
            if m % 2:
                p = 1
                q = math.floor(n / m - 2) + 1
                if not q % 2:
                    q += 1
            else:
                p = 2
                q = math.floor(2 * n / m - 2) + 1
        else:
            p = 1
            q = math.floor(n / m - 2) + 1
            if (m * q) % 2:
                q += 1
    else:
        if n % 2:
            q = 1
            p = math.ceil(m / n)
            if (p + m) % 2:
                p += 1
        else:
            q = 0
            p = 1
    print((n * p + m * q) // 2)