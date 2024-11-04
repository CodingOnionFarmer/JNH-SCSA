n = int(input())
grundy = [0, 0, 1]
for point in range(3, n + 1):
    split = point - 2
    possible = set()
    for small in range((split >> 1) + 1):
        big = split - small
        possible.add(grundy[big] ^ grundy[small])
    g = 0
    while True:
        if g in possible:
            g += 1
            continue
        grundy.append(g)
        break
if grundy[n]:
    print(1)
else:
    print(2)
