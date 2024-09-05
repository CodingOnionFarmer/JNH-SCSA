"""
BOJ : 배열 돌리기 1

풀이 날짜 : 2024.09.05(목)
시작 시간 : 5시 11분
구상 완료 : 5시 11분
제출 시간 : 5시 26분
"""

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
rotated_arr = [[0] * m for _ in range(n)]

# layer 단위로 돌기
for depth in range(min(n >> 1, m >> 1)):
    layer = []
    # 반시계 방향으로 돌면서 넣어주기
    for i in range(depth, n - depth):
        layer.append(arr[i][depth])
    for j in range(depth + 1, m - 1 - depth):
        layer.append(arr[n - 1 - depth][j])
    for i in range(n - 1 - depth, depth - 1, -1):
        layer.append(arr[i][m - 1 - depth])
    for j in range(m - 2 - depth, depth, -1):
        layer.append(arr[depth][j])
    size = len(layer)
    
    # 예를 들어 size가 14이고 r이 2면, layer[-2]부터 순차적으로 넣어주면 2만큼 회전한 효과와 같다.
    idx = -(r % size)

    for i in range(depth, n - depth):
        rotated_arr[i][depth] = layer[idx]
        idx += 1
    for j in range(depth + 1, m - 1 - depth):
        rotated_arr[n - 1 - depth][j] = layer[idx]
        idx += 1
    for i in range(n - 1 - depth, depth - 1, -1):
        rotated_arr[i][m - 1 - depth] = layer[idx]
        idx += 1
    for j in range(m - 2 - depth, depth, -1):
        rotated_arr[depth][j] = layer[idx]
        idx += 1

for line in rotated_arr:
    print(*line)
