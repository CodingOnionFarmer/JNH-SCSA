T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    ans = 0
    start = [0] * n
    end = [0] * n
    for i in range(n):
        s, e = map(int, input().split())
        start[i] = (min(s, e) - 1) >> 1
        end[i] = (max(s, e) - 1) >> 1
    start.sort()
    end.sort()
    pointerS = 0
    pointerE = 0
    ans = 0
    students = 0
    while pointerS < n:
        if start[pointerS] <= end[pointerE]:
            students += 1
            if students >= ans:
                ans = students
            pointerS += 1
        else:
            students -= 1
            pointerE += 1
    print(f'#{tc} {ans}')
