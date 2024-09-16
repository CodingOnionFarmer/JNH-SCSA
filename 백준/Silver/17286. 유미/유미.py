sx, sy = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(3)]
shortest = 120


def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


for a, b, c in ((0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)):
    distance = dist(sx, sy, *people[a]) + dist(*people[a], *people[b]) + dist(*people[b], *people[c])
    if distance < shortest:
        shortest = distance
print(int(shortest))
