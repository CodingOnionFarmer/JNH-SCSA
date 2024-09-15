"""
240915
BOJ : 육각형 우리 속의 개미

시작 시간 : 3시 07분
구상 완료 : 3시 17분
1회 틀림 : 4시 05분 (시간 초과)
제출 완료 : 4시 14분

"""

# DFS로 변경
# 비트마스킹(선택)

# 육각형을 위아래로 찌부시켜서 직사각형으로 만들어 생각
# 최대 14*24 사이즈 필요 (홀짝성 따질거니까 짝수로)

# 가로세로 인덱스 합이 짝수면 아래쪽, 홀수면 위쪽으로만 이동 가능
directions_even_and_odd = (((0, 1), (1, 0), (0, -1)), ((0, 1), (0, -1), (-1, 0)))

# 1차원 좌표로 압축시키고 인접 리스트 만들기
adj = [tuple((i + di) % 14 * 24 + (j + dj) % 24 for di, dj in directions_even_and_odd[i + j & 1]) for i in
       range(14) for j in range(24)]
visited = [False] * 336
visited[0] = True
visited[24] = True

move = int(input())


# 직전에 온 방향을 아예 거르는 방법도 생각해보기
def dfs(depth, now, before):
    if depth == move:
        return sum(visited[nex] for nex in adj[now]) - 1
    cnt = 0
    for nex in adj[now]:
        if not visited[nex]:
            visited[nex] = True
            cnt += dfs(depth + 1, nex, now)
            visited[nex] = False
    return cnt


print(dfs(1, 24, 0))
