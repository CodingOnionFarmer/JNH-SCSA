"""
241003
BOJ : Every? Only One's Marble

시작 시간 : 09시 39분
구상 완료 : 09시 41분
1회 오답 : 10시 12분  (런타임 에러)
제출 완료 : 10시 18분

"""

# n-1번 무인도
# 2n- 2 사회복
# 3n-3 우주여행

n, s, w, g = map(int, input().split())
size = n * 4 - 4
gold_cards = [tuple(map(int, input().split())) for _ in range(g)]
board = [('S',)]
for _ in range(n - 2):
    board.append(tuple(input().split()))
board.append(('D',))  # desert island
for _ in range(n - 2):
    board.append(tuple(input().split()))
board.append(('W',))  # welfare fund
for _ in range(n - 2):
    board.append(tuple(input().split()))
board.append(('T',))  # (space) travel
for _ in range(n - 2):
    board.append(tuple(input().split()))


def game():
    welfare_fund = 0
    stuck_in_desert_island = 0
    now = 0
    cash = s
    bought = [False] * size
    g_idx = 0
    i = int(input())
    for _ in range(i):
        d1, d2 = map(int, input().split())
        if stuck_in_desert_island:
            if d1 == d2:
                stuck_in_desert_island = 0
            else:
                stuck_in_desert_island -= 1
            continue
        d = d1 + d2
        now += d
        if now >= size:
            now -= size
            cash += w
        if now >= size:
            now -= size
            cash += w
        order = board[now][0]
        if order == 'G':
            card_order, card_num = gold_cards[g_idx]
            if card_order == 1:
                cash += card_num
            elif card_order == 2:
                cash -= card_num
                if cash < 0:
                    print('LOSE')
                    return
            elif card_order == 3:
                cash -= card_num
                if cash < 0:
                    print('LOSE')
                    return
                welfare_fund += card_num
            else:
                now += card_num
                if now >= size:
                    now -= size
                    cash += w
                order = board[now][0]
            g_idx += 1
            if g_idx == g:
                g_idx = 0
        if order == 'L':
            if not bought[now]:
                if cash >= int(board[now][1]):
                    cash -= int(board[now][1])
                    bought[now] = True
        elif order == 'D':
            stuck_in_desert_island = 3
        elif order == 'W':
            cash += welfare_fund
            welfare_fund = 0
        elif order == 'T':
            now = 0
            cash += w
    for i in range(size):
        if board[i][0] == 'L' and not bought[i]:
            print('LOSE')
            return
    print('WIN')
    return


game()
