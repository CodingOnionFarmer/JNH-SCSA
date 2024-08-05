n, l, r, x = map(int, input().split())
difficulty = list(map(int, input().split()))
difficulty.sort(reverse=True)


def dfs(hardest, easiest, depth, total):
    if total > r:
        return 0
    if depth == n:
        if total >= l and hardest - easiest >= x:
            return 1
        return 0
    return dfs(hardest, easiest, depth + 1, total) + dfs(hardest, difficulty[depth], depth + 1,
                                                         total + difficulty[depth])


ans = 0
for quiz in range(0, n - 1):
    ans += dfs(difficulty[quiz], difficulty[quiz], quiz + 1, difficulty[quiz])
print(ans)
