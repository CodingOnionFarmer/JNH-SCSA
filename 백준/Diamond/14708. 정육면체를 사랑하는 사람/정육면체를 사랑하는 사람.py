k = int(input())
n = int((k - 1) ** (1 / 3)) + 1
m = int((k // 4) ** (1 / 3))
box = 3 * (n + 1) ** 2
for a in range(max(1, m, n - 1000), n + 1):
    j = (k - 1) // a + 1
    p = int(j ** (1 / 2))
    for b in range(a, min(p, j // a) + 1):
        c = (k - 1) // (a * b) + 1
        if a * b + b * c + c * a < box:
            box = a * b + b * c + c * a
            x = a
            y = b
            z = c
print(x, y, z)
