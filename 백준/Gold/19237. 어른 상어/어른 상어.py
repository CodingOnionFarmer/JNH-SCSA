"""
BOJ : 어른 상어

시작 시간 : 3시 52분
구상 완료 : 4시 49분
제출 시간 : 5시 37분


############################
아래 부분은 코드를 단 한 자도 적기 전에 이미 화가 잔뜩 난 채로 작성했다...

'각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.'
'그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.'
'우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.'
'상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.'
-> 그래서 상하좌우 다 다른 상어 냄새면 이동 한다는 거임 못 한다는 거임??????????? 도대체 이런 필수적인 설명이 왜 없는것이지???

'맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 따라서 처음부터 이동을 못 하는 경우는 없다.'
-> 이게 대체 뭔소리야? 상어 있는칸으로는 이동못한다고 한마디도 안써있는데 어느 맥락에서 '따라서'가 나오는 것이지??????????????
    이동 못하는 조건은 안 말해놓고 '따라서'라는 단어 보고 맥락을 유추하라는 건가???


-> 이 두 가지를 가지고
    '처음에는 인접 칸 중 빈 칸이 있어서 (거긴 냄새가 없으니까) 그리로 이동하고 나면 항상 직전에 있던 내 냄새가 있는 칸으로 이동 가능하므로,
    수학적 귀납법(첫 번째 스텝에서 이동 가능하고, 'k번째 스텝에서 이동 가능하면 k+1번째 스텝에서도 이동 가능'하므로)으로
    상하좌우 모두 내 냄새가 없고 다른 상어 냄새만 있는 칸이 되는 경우는 없다'
    라는 걸 유추해야 되는 건 그냥 설명 부족이라고 생각한다.
    +) 심지어, k가 1일 때는 이 설명으로도 부족하고(직전 칸에 있던 내 냄새가 지워지므로), 더 엄밀한 논증이 필요하다.
        (이 경우, 직전 칸이 항상 빈 칸이 된다는 논증이 필요하게 된다)

    또, 이걸 유추하고 나서야 '따라서 처음부터 이동을 못 하는 경우는 없다'는 문장을 보고,
    '상하좌우 모두 내 냄새가 없고 다른 상어 냄새만 있는 칸이 되는 경우'에는 이동하지 못한다는 사실도 역으로 유추해야 한다.
    이건 그냥 말이 안 된다. 문제 본문이 성의가 없어도 너무 없다.


문제 본문에서
'각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.'
'그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.'
-> 이 뒤에 '그런 칸도 없으면 이동하지 못한다.' 라고 딱 한마디 적어놓기만 해도 설명이 명확한데,
    굳이 이렇게까지 설명 생략하고 억지 논리로 짜맞춰야 하나?
    너무 어이가 없어서 질문 게시판에 가 보니 이미 4년 전부터 같은 의문을 표하는 사람들 투성이다.

+) 문제 조건에 따르면 M은 절대 N^2이 될 수 없다. 범위도 문제 조건하고 안 맞는다.
    -> 이것 때문에 혼란이 더 가중되었다.

###########################

... 하지만 그래서 내가 뭘 할 수 있는데? (사실 이게 중요)
    -> 문제 설명이 조악하고 불명확하고 억지라고 화내봤자, 문제를 보이콧할 수도 없고, 전원 정답 처리해줄 리도 없다. 결국 때려맞춰야 한다.

-> 만약 실전 역량 테스트에서도 이 정도로 성의없는 설명으로 문제가 나오면, 그냥 설명을 해석 가능한 방식 모두 다 시도해보고,
테스트케이스 맞게 나올 때까지 Trial and Error를 해 보는 수밖에 없다고 생각했다. (이런 걸 질문해도 안 받아줄 것 같으므로)
그리고 내가 대충 읽은 게 아니라면 열 번 스무 번 읽어봤자 부실한 설명이 추가되는 건 아니므로,
안 써있는 설명 유추하는 데 시간 낭비하기보다는 이러한 Trial and Error를 하는 편이 더 빠르기도 하다.

결론 : (문제 설명이) 최악인 경우에 어떻게 해야 꾸역꾸역 정답을 맞출 수 있을 지 고민해 봤다는 점에 의의를 두었다.

############################
"""

directions = ((), (-1, 0), (1, 0), (0, -1), (0, 1))  # 1위 2아래 3왼 4오른

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sharks = [0] * (m + 1)
now_seeing = [0] + list(map(int, input().split()))  # 현재 보는 방향
sdp = [[None, ] for _ in range(m + 1)]  # sharks' direction priority

for i in range(1, m + 1):
    for j in range(4):
        sdp[i].append(tuple(map(int, input().split())))

alive = [i for i in range(1, m + 1)]
scent = [[set() for _ in range(n)] for _ in range(n)]
srt = [[[0] * (m + 1) for _ in range(n)] for _ in range(n)]  # scent remain time

for i in range(n):
    for j in range(n):
        if board[i][j]:
            num = board[i][j]
            sharks[num] = i * n + j
            scent[i][j].add(num)
            srt[i][j][num] = k

# def oob(x, y):
#     if 0 <= x < n and 0 <= y < n:
#         return False
#     return True
oob = [[False] * n + [True] for _ in range(n)] + [[True] * n]


def solve():
    global sharks, board, alive
    for second in range(1, 1001):
        sharks_moved = [0] * (m + 1)
        board_moved = [[0] * n for _ in range(n)]
        will_be_dead = set()
        for shark in alive:
            cx, cy = sharks[shark] // n, sharks[shark] % n
            cd = now_seeing[shark]
            no_scent_block = False
            for nd in sdp[shark][cd]:
                dx, dy = directions[nd]
                nx, ny = cx + dx, cy + dy
                if oob[nx][ny]:
                    continue
                if scent[nx][ny]:
                    continue
                no_scent_block = True
                now_seeing[shark] = nd
                sharks_moved[shark] = nx * n + ny
                if not board_moved[nx][ny]:
                    board_moved[nx][ny] = shark
                else:
                    will_be_dead.add(shark)
                break
            if not no_scent_block:
                for nd in sdp[shark][cd]:
                    dx, dy = directions[nd]
                    nx, ny = cx + dx, cy + dy
                    if oob[nx][ny]:
                        continue
                    if srt[nx][ny][shark]:
                        now_seeing[shark] = nd
                        sharks_moved[shark] = nx * n + ny
                        if not board_moved[nx][ny]:
                            board_moved[nx][ny] = shark
                        else:
                            will_be_dead.add(shark)
                        break

        for i in range(n):
            for j in range(n):
                scent_disappear = set()
                for s in scent[i][j]:
                    srt[i][j][s] -= 1
                    if not srt[i][j][s]:
                        scent_disappear.add(s)
                scent[i][j] -= scent_disappear

        for shark in alive:
            sx, sy = sharks_moved[shark] // n, sharks_moved[shark] % n
            scent[sx][sy].add(shark)
            srt[sx][sy][shark] = k

        sharks = sharks_moved
        board = board_moved
        alive = [a for a in alive if a not in will_be_dead]

        # print('=======================')
        # print(second, '초')
        # for line in board:
        #     print(line)
        # print(alive)

        if len(alive) == 1:
            print(second)
            return
    print(-1)
    return


solve()
