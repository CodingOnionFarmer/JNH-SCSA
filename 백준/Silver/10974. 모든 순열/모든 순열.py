n = int(input())
sequence = []
chosen = [False] * (n + 1)


def dfs(depth):
    if depth == n:
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
