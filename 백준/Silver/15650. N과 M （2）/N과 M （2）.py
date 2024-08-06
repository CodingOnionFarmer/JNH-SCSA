n, m = map(int, input().split())
sequence = []


# 오름차순이므로 지금까지 고른 것 중 가장 큰 수(=직전에 고른 수)가 biggest
def dfs(depth, biggest):
    if depth == m:
        print(*sequence)
        return
    # range 범위를 조절해서 남은 개수로 다 못 고르는 경우는 미리 배제
    for num in range(biggest + 1, n - m + depth + 2):
        sequence.append(num)
        dfs(depth + 1, num)
        sequence.pop()


dfs(0, 0)
