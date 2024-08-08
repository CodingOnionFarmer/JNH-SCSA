# dfs, 백트래킹
# 2차원 배열을 직접 변형하면서 하면 매우 비효율적이다.
# 비트연산으로 앞선 퀸들과 수직 또는 양쪽 대각선으로 만나는지 판정하도록 하여 성능을 향상시켰다.


n = int(input())


def dfs(depth, vertical, diagonal_right, diagonal_left):
    if depth == n:
        return 1
    ban = vertical | diagonal_right | diagonal_left
    cnt = 0
    for i in range(n):
        put = 1 << i
        if put & ban:
            continue
        cnt += dfs(depth + 1, vertical | put, (diagonal_right | put) >> 1, (diagonal_left | put) << 1)
    return cnt


half = n >> 1
ans = 0

# i-1이나 half-1이 음수일 수도 있으므로, 비트 연산 >>를 할 때 주의한다.
for i in range(half):
    ans += dfs(1, 1 << i, 1 << i >> 1, 1 << (i + 1))
ans <<= 1
if n & 1:
    ans += dfs(1, 1 << half, 1 << half >> 1, 1 << (half + 1))
print(ans)
