"""
BOJ : 상어 중학교

시작 시간 : 2시 10분
구상 완료 : 2시 13분
제출 시간 : 3시 08분

"""

#################
# 메모
# -1 검정, 0 무지개, 1~m 일반
# 그럼 빈 칸은? -2로 하자


#################


# 입력 처리
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 룩업 테이블 구성
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
oob = [[False] * n + [True] for _ in range(n)] + [[True] * n]
adj = [[[(i + di, j + dj) for di, dj in directions if not oob[i + di][j + dj]] for j in range(n)] for i in range(n)]


# 필요한 함수 구현
# 1. 중력 함수

def gravity():
    for c in range(n):
        bottom = n - 1  # 블록이 쌓일 곳
        for r in range(n - 1, -1, -1):
            num = board[r][c]
            if num == -2:  # 빈칸
                continue
            elif num == -1:  # 검정
                bottom = r - 1  # 바닥이 검정 바로 위가 됨
            else:  # 나머지
                board[r][c] = -2  # 있던 칸 비우기
                board[bottom][c] = num  # 바닥에 떨어짐
                bottom -= 1  # 바닥 한 칸 올림
    return


# 90도 반시계 회전
def rotate():
    for i in range((n + 1) >> 1):
        ri = n - 1 - i
        for j in range(n >> 1):
            rj = n - 1 - j
            board[i][j], board[j][ri], board[ri][rj], board[rj][i] = board[j][ri], board[ri][rj], board[rj][i], \
                board[i][j]
    return


# 그룹 찾는 함수
def find_groups():
    # 구현 도중 아이디어 : visited에 블록 번호를 매겨놓으면,
    # 무지개 블록 visited 판정 로직이 명료해진다 (현재 탐색 중인 번호랑 같으면 이미 visited, 다르면 not visited)
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            block = board[i][j]
            if block > 0:
                if visited[i][j]:
                    continue
                visited[i][j] = block
                q = [(i, j)]
                size = 1
                rainbow_cnt = 0
                while q:
                    nq = []
                    for ci, cj in q:
                        for ni, nj in adj[ci][cj]:
                            next_block = board[ni][nj]
                            if next_block == block:
                                if not visited[ni][nj]:
                                    visited[ni][nj] = block
                                    size += 1
                                    nq.append((ni, nj))
                            elif not next_block:
                                if visited[ni][nj] != block:
                                    visited[ni][nj] = block
                                    size += 1
                                    rainbow_cnt += 1
                                    nq.append((ni, nj))
                    q = nq
                if size > 1:
                    groups.append((size, rainbow_cnt, i, j))
    return


# 선택한 그룹 지우는 함수
def erase(i, j):
    num = board[i][j]
    board[i][j] = -2  # 빈칸은 -2
    q = [(i, j)]
    while q:
        nq = []
        for ci, cj in q:
            for ni, nj in adj[ci][cj]:
                if board[ni][nj] in (0, num):
                    board[ni][nj] = -2
                    nq.append((ni, nj))
        q = nq
    return


# 메인 파트 구현
# 그룹 찾기는 함수화하지 않았음

score = 0
while True:
    # 크기, 무지개블록수, 기준블록좌표 순으로 정렬
    # 이 중 고유한 값은 기준블록좌표
    groups = []
    find_groups()
    if not groups:
        break

    # 그룹이 있으면, 그 중 최우선인 것 뽑아서 점수 얻고 삭제
    size, rainbow, i, j = max(groups)
    score += size ** 2
    erase(i, j)

    # 중력 회전 중력
    gravity()
    rotate()
    gravity()

print(score)
