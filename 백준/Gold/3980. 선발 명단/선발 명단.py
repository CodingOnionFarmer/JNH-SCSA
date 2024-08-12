def dfs(depth, occupied):
    if depth == 11:
        return 0
    if not memo[occupied]:
        tmp_max = -1100
        for pos in ability_not_zero[depth]:
            if (1 << pos) & occupied:
                continue
            tmp = dfs(depth + 1, (1 << pos) | occupied) + ability[depth][pos]
            if tmp > tmp_max:
                tmp_max = tmp
        memo[occupied] = tmp_max
    return memo[occupied]


T = int(input())
for tc in range(T):
    ability = [list(map(int, input().split())) for _ in range(11)]
    ability_not_zero = [[idx for idx, ab in enumerate(ability[i]) if ab] for i in range(11)]
    memo = [0] * 2048
    print(dfs(0, 0))
