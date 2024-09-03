"""
BOJ : 구슬 탈출 2

시작 시간 : 3시 39분
구상 완료 : 3시 41분
테케 틀림 : 3시 49분
제출 시간 : 3시 52분
"""

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    height = board[i][0]
    same = 0
    lift = 0
    line = True
    for h in board[i]:
        if h == height:
            if lift:
                lift -= 1
            else:
                same += 1
        elif lift or h > height + 1 or h < height - 1:
            line = False
            break
        elif h == height + 1:
            if same < l:
                line = False
                break
            else:
                height = h
                same = 1
        else:
            height = h
            lift = l - 1
            same = 0
    if lift:
        line = False
    # if line:
    #     print(i, '행')
    ans += line

for j in range(n):
    height = board[0][j]
    same = 0
    lift = 0
    line = True
    for i in range(n):
        h = board[i][j]
        if h == height:
            if lift:
                lift -= 1
            else:
                same += 1
        elif lift or h > height + 1 or h < height - 1:
            line = False
            break
        elif h == height + 1:
            if same < l:
                line = False
                break
            else:
                height = h
                same = 1
        else:
            height = h
            lift = l - 1
            same = 0
    if lift:
        line = False
    # if line:
    #     print(j, '열')
    ans += line

print(ans)
