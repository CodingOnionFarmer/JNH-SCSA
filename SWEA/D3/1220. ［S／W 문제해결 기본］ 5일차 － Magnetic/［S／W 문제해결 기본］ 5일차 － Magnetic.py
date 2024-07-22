for tc in range(1, 11):
    n = int(input())
    table = [input() for _ in range(100)]
    ans = 0
    for c in range(0, 199, 2):
        N = False
        S = False
        for r in range(100):
            if table[r][c] == '1' and not N:
                N = True
                S = False
            elif table[r][c] == '2' and not S:
                S = True
                if N:
                    ans += 1
                    N = False
    print(f'#{tc} {ans}')
