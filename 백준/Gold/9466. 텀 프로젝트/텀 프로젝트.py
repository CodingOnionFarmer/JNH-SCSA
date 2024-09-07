T = int(input())
for tc in range(1, T + 1):
    n = int(input()) + 1
    want_to_be_group = [0] + list(map(int, input().split()))
    representative = [0] * n
    depth = [0] * n
    students_in_team = 0
    for i in range(1,n):
        if representative[i]:
            continue
        representative[i] = i
        now = i
        size = 1
        while True:
            now = want_to_be_group[now]
            if representative[now]:
                if representative[now] == i:
                    students_in_team += size - depth[now]
                break
            representative[now] = i
            depth[now] = size
            size += 1
    print(n - students_in_team - 1)
