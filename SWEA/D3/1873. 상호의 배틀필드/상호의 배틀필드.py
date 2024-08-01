# 4회차 제출
# 복습 이후 배운 내용 반영 + 주석 추가

# 시뮬레이션 + 구현을 시키는 대로 잘 수행하면 된다.
# 방향에 관해 반복적으로 사용하는 것들은 0,1,2,3 순서를 맞춰서 tuple, string, dictionary로 만들었다.
# 반복적으로 사용되는 기능들은 함수로 만들었다.
# 변수명이나 함수명을 의미가 잘 통하도록 만들거나, 주석을 달아서 가독성을 높이도록 노력하였다.


t = int(input())

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 0위 1오른 2아래 3왼쪽 방향

tank_state_rev = '^>v<'
tank_state = {char: idx for idx, char in enumerate(tank_state_rev)}  # dictionary comprehension

move_command = {'U': 0, 'R': 1, 'D': 2, 'L': 3}


def find_tank():
    for i in range(h):
        for j in range(w):
            if board[i][j] in tank_state:  # 탱크 찾으면
                global cr, cc, cd  # 행위치,열위치,바라보는 방향 저장 (전역변수 변경 위해 global 선언)
                cr = i
                cc = j
                cd = tank_state[board[i][j]]
                board[i][j] = '.'
                # 끝날 때까지 굳이 탱크 위치를 board를 변경시키면서 표시할 필요 없음
                # 끝나기 전까지는 탱크 위치도 그냥 평지('.')로 표시하고 탱크의 위치와 방향을 cr,cc,cd 변수로 관리
                return


def shoot(d):  # d는 방향값(0,1,2,3 중 하나)
    di, dj = direction[d]  # 현재 보는 방향
    ci, cj = cr, cc  # 현재 탱크 위치
    while True:
        ci += di
        cj += dj
        if board[ci][cj] == '*':  # 벽돌벽 파괴
            board[ci][cj] = '.'
            return
        if board[ci][cj] == '#':  # 강철벽 파괴 못함
            return


# def move(d):
    # move 기능도 기능이 복잡하다면 함수화하면 좋다.
    # 만약 만든다면 전역변수인 cr,cc,cd의 값을 변경하기 위해 global 선언을 해 줘야 할 것


for tc in range(1, t + 1):
    h, w = map(int, input().split())
    board = [list(input()) + ['#'] for _ in range(h)] + [['#'] * w]
    # board의 맨 밑줄, 맨 오른쪽 열에 탈출 방지용 강철벽을 쳐 두었다.
    # 맨 위나 맨 왼쪽 밖으로 탈출해도, index가 -1이면 맨 끝으로 가므로, 왼쪽과 위쪽에도 벽을 쳐 둔 효과가 있다.
    cr, cc, cd = 0, 0, 0  # 현재 행위치, 열위치, 바라보는 방향
    find_tank()
    n = int(input())
    command = input()
    for action in command:
        if action == 'S':
            shoot(cd)
        else:  # 발사가 아닌 액션은 전부 이동
            # -------------------
            cd = move_command[action]  # 바라보는 방향 돌리기
            dr, dc = direction[cd]  # 바라보는 방향 이동 시도
            if board[cr + dr][cc + dc] == '.':  # 평지면 이동
                cr += dr
                cc += dc
            # 이 부분이 복잡하지 않아서 안 만들었는데, move 함수로 만들었다면
            # move(move_command[action])을 실행하면 될 것이다.
            # -------------------
    board[cr][cc] = tank_state_rev[cd]  # 모든 명령 수행 후에 게임판에 탱크 표시
    board.pop()  # 경계 탈출 방지용 맨 마지막 행 삭제
    print(f'#{tc} ', end='')
    for line in board:
        line.pop()  # 경계 탈출 방지용 맨 마지막 열 삭제
        print(''.join(line))
