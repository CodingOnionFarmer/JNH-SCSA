for tc in range(1, int(input()) + 1):
    n = int(input())
    ans = 0
    half = n // 2
    for i in range(half):
        line = input()
        for j in range(half - i, half + i + 1):
            ans += int(line[j])
    for i in range(half + 1):
        line = input()
        for j in range(i, n - i):
            ans += int(line[j])
    print(f'#{tc} {ans}')
