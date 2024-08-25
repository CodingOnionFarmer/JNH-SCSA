# 구현, 완전 탐색

# 조금 더 Greedy한 탐색 (중복된 탐색 피하기)

# 오목 가일수 승리 판정 문제와 비슷한 반례 찾음 (맨 왼쪽에서 한 칸 왼쪽을 바꾸는 경우를 count안함)
# Greedy가 이렇게 위험합니다...

# 그 외에도 수많은 무시무시한 논리적 오류 고치기

n = int(input())
board = [list(input()) + [None] for _ in range(n)] + [[None] * (n + 1)]
most_candy = 1

# 가로 탐색
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        candy = board[i][j]
        amount = 1
        changed = False
        for k in range(j + 1, n):
            if board[i][k] == candy:
                visited[i][k] = True
                amount += 1
                continue
            if changed:
                break

            # 여기서부터 중요
            # 위아래랑 바꾸기
            if board[i - 1][k] == candy or board[i + 1][k] == candy:
                changed = True
                amount += 1
                continue
            # 오른쪽이랑 바꾸기
            if board[i][k + 1] == candy:
                amount += 1
                changed = True
                break
            break
        # 예외처리 : 맨 왼쪽보다 한 칸 왼쪽 바꾸기
        if not changed:
            if board[i - 1][j - 1] == candy or board[i + 1][j - 1] == candy:
                amount += 1
            elif j and board[i][j - 2] == candy:
                amount += 1
        if amount > most_candy:
            most_candy = amount

# 세로 탐색
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        candy = board[i][j]
        amount = 1
        changed = False
        for k in range(i + 1, n):
            if board[k][j] == candy:
                visited[k][j] = True
                amount += 1
                continue
            if changed:
                break

            # 좌우랑 바꾸기
            if board[k][j - 1] == candy or board[k][j + 1] == candy:
                changed = True
                amount += 1
                continue
            # 아래랑 바꾸기
            # 오타 조심
            if board[k + 1][j] == candy:
                amount += 1
                changed = True
                break
            break
        # 예외처리 : 맨 위보다 한 칸 위쪽 바꾸기
        if not changed:
            if board[i - 1][j - 1] == candy or board[i - 1][j + 1] == candy:
                amount += 1
            elif i and board[i - 2][j] == candy:
                amount += 1
        if amount > most_candy:
            most_candy = amount

print(most_candy)
