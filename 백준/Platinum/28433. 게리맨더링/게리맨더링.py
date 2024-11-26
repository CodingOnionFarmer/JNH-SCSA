import sys

input = sys.stdin.readline
for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    p = 0
    m = 0
    x = 0
    y = 0
    for i in range(n):
        if arr[i] > 0:
            p += 1
            if y:
                if x:
                    if x + y > 0:
                        x = arr[i]
                    elif arr[i] + y > 0:
                        x = arr[i] + y
                    else:
                        m += 1
                        x = arr[i]
                else:
                    if arr[i] + y > 0:
                        x = arr[i] + y
                    else:
                        m += 1
                        x = arr[i]
                y = 0
            else:
                x = arr[i]
        elif arr[i] < 0:
            if x:
                if x + y > 0 >= x + y + arr[i]:
                    x = 0
                    y = 0
            y += arr[i]
    if y:
        if x + y <= 0:
            m += 1
    # print(p, m)
    if p > m:
        print('YES')
    else:
        print('NO')
