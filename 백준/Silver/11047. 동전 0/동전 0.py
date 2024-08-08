n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
ans = 0
for i in range(n - 1, 0, -1):
    use = k // coins[i]
    ans += use
    k -= use * coins[i]
ans += k // coins[0]
print(ans)
