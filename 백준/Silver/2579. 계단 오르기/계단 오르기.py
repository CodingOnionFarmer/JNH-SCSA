# Dynamic Programming

n = int(input())
if n < 3:
    print(sum(int(input()) for _ in range(n)))
else:
    dp2 = int(input())  # 2계단 밑
    dp12 = int(input())  # 1계단 밑, 최근 이동 2칸
    dp11 = dp12 + dp2  # 1계단 밑, 최근 이동 1칸
    for i in range(n - 2):
        score = int(input())  # 탐색 위치
        
        # 다음 칸 기준 2계단 밑의 최대 : 1계단 밑이었던 것들 중 최대
        # 다음 칸 기준 1계단 밑인 것들 : 2가지
        # 최근 이동 2칸이려면 2칸 밑(dp2)에서 score 더해줌
        # 최근 이동 1칸이려면 1칸 밑 + 최근이동2칸(dp12)에서 score 더해줌.
        dp2, dp12, dp11 = max(dp12, dp11), dp2 + score, dp12 + score
    print(max(dp12, dp11))
