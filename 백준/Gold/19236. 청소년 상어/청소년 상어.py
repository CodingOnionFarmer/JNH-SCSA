"""
BOJ : 청소년 상어

시작 시간 : 9시 38분
구상 완료 : 9시 42분
제출 시간 : 10시 22분
소요 시간 : 44분
실패 횟수 : 0회
사용 메모리 : 111408KB
실행 시간 : 96ms  (제출 시점 기준 PyPy3 1위, 96ms가 두명 더 있으나 최소 메모리로 1등)


#########################
자가 피드백(Good)
1. 함수화를 안 할 수 있으면 굳이 안 하는 편이지만, 이 문제는 두 작업을 분리해서 함수화하는게 좋다고 판단했다.
    -> 구현하는 내용이 섞이지 않고 기능이 구분되어 구현하기 쉬웠다.

2. 컨디션 난조에서도 푸는 연습을 해 볼 수 있었다.

3. 내 개인적인 기준으로 다소 비효율적이더라도, 문제를 통과하는데 전혀 지장없는 수준인 것들은 쉽게 쉽게 구현했다.
    -> 그래도 1등이라 기분이 더 좋다.

########################
자가 피드백(Bad)
1. 비효율적인 거(alive 같은거 백트래킹하면 이전상태로 돌려야 되는데 매우매우 비효율적으로 돌아간다) 리팩토링 하고싶다.

2. 마음이 급해서 그랬는지 풀면서는 주석을 안 달았다.
    -> 주석을 달면서 해야 () <= 바깥, (0,0) <- 빈칸, (-1,d) <- 상어 이거 세 가지를 조금이라도 덜 헷갈릴 것인데,
    -> 안 달고 했다가 상어 위치를 -1이 아니라 0으로 표시하는 실수를 한 번 해서 잠깐 디버깅했다.
"""

# 브루트포스, 백트래킹

directions = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

board = [[()] * 5 for _ in range(5)]  # 4x4 바깥은 () (빈 튜플)로 패딩
where_is_the_fish = [None for _ in range(17)]  # 1~16번 물고기가 어디 있는지 표시
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = (line[j << 1], line[j << 1 | 1] - 1)
        where_is_the_fish[line[j << 1]] = (i, j)

alive = [True] * 17  # 1~16번 물고기가 살아있는지 표시
ans = board[0][0][0]  # 처음에 0,0 자리 물고기를 먹고 시작한다.
alive[ans] = False
board[0][0] = [-1, board[0][0][1]]  # 상어는 -1로 표시했다.


# 물고기가 움직이는 단계, 움직이고 난 뒤의 보드 뿐만 아니라, 메인 함수에서 백트래킹할 때 원복을 위해
# 움직이기 전 상태의 where_is_the_fish 배열도 함께 return한다
# (이 부분이 매우 비효율적이지만 다 합쳐도 얼마 안 되는 연산이라 그냥 했다)
def fish_move(brd):
    temp = [[fish[:] for fish in line] for line in brd]
    originally_where = where_is_the_fish[:]
    for f in range(1, 17):
        # 살아있는 것들만 이동
        if alive[f]:
            # f번 물고기의 위치와 방향 찾기
            fi, fj = where_is_the_fish[f]
            fd = temp[fi][fj][1]
            # 문제 조건 상 8방향 중 어딘가로는 반드시 이동할 수 있다.
            for turn in range(8):
                di, dj = directions[fd]
                ni, nj = fi + di, fj + dj
                # 이동 가능한지 판정하고, 불가능하면 반시계 방향으로 45도 회전
                if not temp[ni][nj] or temp[ni][nj][0] == -1:
                    fd = (fd + 1) % 8
                    continue
                # 이동하려는 곳이 빈 칸
                if temp[ni][nj][0] == 0:
                    temp[fi][fj] = (0, 0)
                    temp[ni][nj] = (f, fd)
                    where_is_the_fish[f] = (ni, nj)
                # 이동하려는 곳이 다른 물고기
                else:
                    temp[fi][fj], temp[ni][nj] = temp[ni][nj], (f, fd)
                    where_is_the_fish[f] = (ni, nj)
                    where_is_the_fish[temp[fi][fj][0]] = (fi, fj)
                # f번 물고기 이동이 완료되면 종료
                break
    # 물고기들이 다 움직이고 난 뒤의 배열 뿐만 아니라 움직이기 전에 위치를 표시해 둔 배열도 같이 반환한다.
    return temp, originally_where


def dfs(brd, si, sj, score):
    # fish_move를 하고 return하기 전에는 where_is_the_fish를 원상태로 되돌려 놓아야 한다.
    # 판 자체는 인자로 주고받으므로 원본이 손상되지 않지만, where_is_the_fish는 원본을 수정하도록 짰기 때문
    # -> 이 부분 리팩토링 필요
    moved_brd, before_moved_where = fish_move(brd)
    can_move = []
    d = moved_brd[si][sj][1]
    di, dj = directions[d]
    # 이동할 수 있는 거리는 최대 3이다.
    for dist in range(1, 4):
        ni, nj = si + di * dist, sj + dj * dist
        if not moved_brd[ni][nj]:
            break
        if moved_brd[ni][nj][0]:
            can_move.append(dist)
    # 이동할 수 있는 곳이 없으면 최고 점수 판정하고 where_is_the_fish 원복하고 종료
    if not can_move:
        global ans
        if score > ans:
            ans = score
        for i in range(17):
            where_is_the_fish[i] = before_moved_where[i]
        return
    # 이동 가능하면 일단 상어가 있던 곳은 빈 칸이 된다.
    moved_brd[si][sj] = (0, 0)
    for dist in can_move:
        ni, nj = si + di * dist, sj + dj * dist
        fish, nd = moved_brd[ni][nj]
        # 이동한 자리의 물고기를 먹어치우고 dfs 탐색하고 먹기 전 상태로 원복
        moved_brd[ni][nj] = (-1, nd)
        alive[fish] = False
        dfs(moved_brd, ni, nj, score + fish)
        moved_brd[ni][nj] = (fish, nd)
        alive[fish] = True
    # return하기전에 where_is_the_fish 원복
    for i in range(17):
        where_is_the_fish[i] = before_moved_where[i]
    return


dfs(board, 0, 0, ans)
print(ans)
