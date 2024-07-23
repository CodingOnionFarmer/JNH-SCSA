for tc in range(1, int(input()) + 1):
    n = int(input())
    farm = [list(map(int, list(input()))) for _ in range(n)]
    ans = 0
    for i in range(n // 2):
        for j in range(n // 2 - i, n // 2 + i + 1):
            ans += farm[i][j]
    for i in range(n // 2, n):
        for j in range(i - n // 2, (n * 3) // 2 - i):
            ans += farm[i][j]
    print(f'#{tc} {ans}')
