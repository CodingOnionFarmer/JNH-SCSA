from functools import cmp_to_key
import sys

input = sys.stdin.readline


def ccw(p, p1, p2):
    x1, y1 = p1[0] - p[0], p1[1] - p[1]
    x2, y2 = p2[0] - p[0], p2[1] - p[1]
    return x1 * y2 - x2 * y1


def compare(p1, p2):
    cp = ccw((0, 0), p1, p2)
    if cp:
        return -cp
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1) + abs(y1) - abs(x2) - abs(y2)


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
sx, sy = min(points)
for i, (x, y) in enumerate(points):
    points[i] = (x - sx, y - sy)

points.sort(key=cmp_to_key(compare))
convex_hull = [points[0], points[1]]
for point in points[2:]:
    while len(convex_hull) > 1 and ccw(convex_hull[-2], convex_hull[-1], point) <= 0:
        convex_hull.pop()
    convex_hull.append(point)
print(len(convex_hull))
