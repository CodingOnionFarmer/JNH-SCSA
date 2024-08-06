# dfs와 재귀를 이용해서 풀 수 있다.


n, m = map(int, input().split())
sequence = []
chosen = [False] * (n + 1)


def dfs(depth):
    if depth == m:
        print(*sequence)
        return
    for num in range(1, n + 1):
        if not chosen[num]:
            sequence.append(num)
            chosen[num] = True
            dfs(depth + 1)
            sequence.pop()
            chosen[num] = False


dfs(0)
