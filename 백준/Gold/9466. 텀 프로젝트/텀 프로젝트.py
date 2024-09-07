T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    want_to_be_group = list(map(int, input().split()))
    visited = [False] * n
    representative = [i for i in range(n)]
    depth = [0] * n
    students_in_team = 0
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        r = i
        now = r
        size = 1
        while True:
            now = want_to_be_group[now] - 1
            if visited[now]:
                if representative[now] == r:
                    students_in_team += size - depth[now]
                break
            visited[now] = True
            representative[now] = r
            depth[now] = size
            size += 1
    print(n - students_in_team)
