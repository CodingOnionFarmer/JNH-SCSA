"""
240915
BOJ : 뱀과 사다리 게임

시작 시간 : 2시 20분
구상 완료 : 2시 28분
제출 시간 : 2시 35분

"""

# BFS
# DP 풀이를 생각해 봤으나 어렵다고 판단, 그리고 BFS로도 시간복잡도가 작은 것 같다.

n, m = map(int, input().split())
snl = [i for i in range(101)] + [1] * 5  # snake and ladder, 패딩을 쳐놔서 100 뒤로 넘어가는 것까지 고려
for l in range(n):
    x, y = map(int, input().split())
    snl[x] = y
for s in range(m):
    u, v = map(int, input().split())
    snl[u] = v

visited = [False] * 101
visited[1] = True
q = [1]
dice = 0
while q and not visited[100]:
    dice += 1
    nq = []
    for num in q:
        for i in range(1, 7):
            move = snl[num + i]
            if not visited[move]:
                visited[move] = True
                nq.append(move)
    q = nq

print(dice)
