import sys

input = sys.stdin.readline

n, m = map(int, input().split())
prefix_sum = [[0] * (m - 7) for _ in range(n)]  # prefix_sum[i][j]는 i행 j열부터 오른쪽으로 8칸에서 체스판과 같은 개수의 합
white_is0 = {'W': 0, 'B': 1}
board = [[0] * m for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(8):
        board[i][j] = (i + j + white_is0[line[j]]) % 2
    s = sum(board[i][:8])
    prefix_sum[i][0] = s
    for j in range(8, m):
        board[i][j] = (i + j + white_is0[line[j]]) % 2
        s += board[i][j]
        s -= board[i][j - 8]
        prefix_sum[i][j - 7] = s

least = 32  # 답이 32 초과인 경우는 없음
for j in range(m - 7):  # 각각의 순회에서도 누적 합 아이디어 응용
    same = 0
    for i in range(8):
        same += prefix_sum[i][j]
    if same < least:
        least = same
    elif 64 - same < least:  # 흑백 반전도 체크
        least = 64 - same
    for i in range(8, n):  # 맨 윗줄 빼고 그 다음줄 더하고 반복
        same += prefix_sum[i][j]
        same -= prefix_sum[i - 8][j]
        if same < least:
            least = same
        elif 64 - same < least:
            least = 64 - same
print(least)
