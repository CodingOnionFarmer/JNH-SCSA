for tc in range(1, int(input()) + 1):
    n = int(input())
    ans = 0
    half = n >> 1
    for i in range(half, 0, -1):
        line = input()
        ans += sum(map(int, line[i:n - i]))
    for i in range(half + 1):
        line = input()
        ans += sum(map(int, line[i:n - i]))
    print(f'#{tc} {ans}')
