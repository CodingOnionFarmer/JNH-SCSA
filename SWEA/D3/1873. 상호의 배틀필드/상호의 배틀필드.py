# 3회차 제출

# 시뮬레이션 + 구현을 시키는 대로 잘 수행하면 된다.
# 방향에 관해 반복적으로 사용하는 것들은 0,1,2,3 순서를 맞춰서 tuple, string, dictionary로 만들었다.
# 반복적으로 사용되는 기능들은 함수로 만들었다.
# 변수명이나 함수명을 의미가 잘 통하도록 만들거나, 주석을 달아서 가독성을 높이도록 노력하였다.


t = int(input())

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 0위 1오른 2아래 3왼쪽 방향

tank_state = {'^': 0, '>': 1, 'v': 2, '<': 3}
tank_state_rev = '^>v<'

move_command = {'U': 0, 'R': 1, 'D': 2, 'L': 3}


def find_tank():
    for i in range(h):
        for j in range(w):
            if board[i][j] in tank_state:
                global cr, cc, cd
                cr = i
                cc = j
                cd = tank_state[board[i][j]]
                board[i][j] = '.'  # 끝날 때까지 굳이 탱크 위치를 board를 변경시키면서 표시할 필요 없음
                return


def shoot(d):
    di, dj = direction[d]  # 현재 보는 방향
    ci, cj = cr, cc  # 현재 탱크 위치
    while True:
        ci += di
        cj += dj
        if board[ci][cj] == '*':
            board[ci][cj] = '.'
            return
        if board[ci][cj] == '#':
            return


for tc in range(1, t + 1):
    h, w = map(int, input().split())
    board = [list(input()) + ['#'] for _ in range(h)] + [['#'] * w]
    cr, cc, cd = 0, 0, 0  # 현재 행위치, 열위치, 바라보는 방향
    find_tank()
    n = int(input())
    command = input()
    for action in command:
        if action == 'S':
            shoot(cd)
        else:
            cd = move_command[action]  # 바라보는 방향 돌리기
            dr, dc = direction[cd]  # 바라보는 방향 이동 시도
            if board[cr + dr][cc + dc] == '.':  # 평지면 이동
                cr += dr
                cc += dc
    board[cr][cc] = tank_state_rev[cd]  # 다 돌리고 나서 게임판의 탱크 위치를 보는 방향대로 바꿔주기
    board.pop()  # 경계 탈출 방지용 맨 마지막 행 삭제
    print(f'#{tc} ', end='')
    for line in board:
        line.pop()  # 경계 탈출 방지용 맨 마지막 열 삭제
        print(''.join(line))
