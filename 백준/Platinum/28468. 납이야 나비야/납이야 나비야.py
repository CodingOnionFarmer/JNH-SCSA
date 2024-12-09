n, m = map(int, input().split())
graph = {i + 1: set() for i in range(n)}
triangle = [0] * (n + 1)
quadrangle = [0] * (n + 1)
answer = 0
for i in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
for x in range(1, n + 1):
    for y in graph[x]:
        t = len(graph[x] & graph[y])
        triangle[x] += t
        quadrangle[x] += t * (t - 1) // 2
    triangle[x] //= 2
    p = len(graph[x])
    t = triangle[x]
    q = quadrangle[x]
    # print(x, p, t, q)
    if p > 5:
        answer += (t * (t - 1) // 2 - q) * (p - 4) * (p - 5) // 2
print(answer)
