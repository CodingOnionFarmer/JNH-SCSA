n, m = map(int, input().split())
prefix_sum = [[0] * (m - 7) for _ in range(n)]  # prefix_sum[i][j]는 i행 j열부터 오른쪽으로 8칸에서 체스판과 같은 개수의 합
for i in range(n):
    line = input()
    if i % 2:
        compare_line = 'WB' * ((m + 1) // 2)
    else:
        compare_line = 'BW' * ((m + 1) // 2)
    s = 0
    for j in range(8):
        if line[j] == compare_line[j]:
            s += 1
    prefix_sum[i][0] = s
    for j in range(8, m):
        if line[j] == compare_line[j]:
            s += 1
        if line[j - 8] == compare_line[j - 8]:
            s -= 1
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
