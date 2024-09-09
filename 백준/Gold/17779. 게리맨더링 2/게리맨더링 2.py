"""
BOJ : 게리맨더링 2

시작 시간 : 9시 21분
구상 완료 : 9시 27분
제출 시간 : 11시 03분
"""

# 브루트포스, 누적 합

n = int(input())
city = [list(map(int, input().split())) for _ in range(n)]
acc_sum = [[0] * n for _ in range(n)]
for i in range(n):
    s = 0
    for j in range(n):
        s += city[i][j]
        acc_sum[i][j] = s

min_diff = 40000  # 20*20*100

for x in range(n - 2):
    for y in range(1, n - 1):
        for d1 in range(1, min(n - 2 - x, y)):
            for d2 in range(1, min(n - 1 - x - d1, n - 1 - y)):
                # if x == 2 and y == 4 and d1 == 2 and d2 == 1:
                #     print('======here======')
                # 선거구 1,2,3,4,5, areas' population
                ap = [0, 0, 0, 0, 0]

                for i in range(x):  # 1/2
                    line = acc_sum[i]
                    ap[0] += line[y]
                    ap[1] += line[n - 1] - line[y]
                    # if x == 2 and y == 4 and d1 == 2 and d2 == 1:
                    #     print(i)
                    #     print(ap)

                if d1 <= d2:
                    for i in range(d1):  # 1/5/2
                        line = acc_sum[x + i]
                        ap[0] += line[y - i - 1]
                        ap[4] += line[y + i] - line[y - i - 1]
                        ap[1] += line[n - 1] - line[y + i]
                    for i in range(d2 - d1 + 1):  # 3/5/2
                        line = acc_sum[x + d1 + i]
                        ap[2] += line[y - d1 + i - 1]
                        ap[4] += line[y + d1 + i] - line[y - d1 + i - 1]
                        ap[1] += line[n - 1] - line[y + d1 + i]
                    for i in range(d1):  # 3/5/4
                        line = acc_sum[x + d2 + i + 1]
                        ap[2] += line[y + d2 - d1 * 2 + i]
                        ap[4] += line[y + d2 - i - 1] - line[y + d2 - d1 * 2 + i]
                        ap[3] += line[n - 1] - line[y + d2 - i - 1]
                else:
                    for i in range(d2 + 1):  # 1/5/2
                        line = acc_sum[x + i]
                        ap[0] += line[y - i - 1]
                        ap[4] += line[y + i] - line[y - i - 1]
                        ap[1] += line[n - 1] - line[y + i]
                        # if x == 2 and y == 4 and d1 == 2 and d2 == 1:
                        #     print(x + i)
                        #     print(ap)
                    for i in range(d1 - d2 - 1):  # 1/5/4
                        line = acc_sum[x + d2 + i + 1]
                        ap[0] += line[y - d2 - i - 2]
                        ap[4] += line[y + d2 - i - 1] - line[y - d2 - i - 2]
                        ap[3] += line[n - 1] - line[y + d2 - i - 1]
                        # if x == 2 and y == 4 and d1 == 2 and d2 == 1:
                        #     print(x + d2 + i + 1)
                        #     print(ap)
                    for i in range(d2 + 1):  # 3/5/4
                        line = acc_sum[x + d1 + i]
                        ap[2] += line[y - d1 + i - 1]
                        ap[4] += line[y - d1 + 2 * d2 - i] - line[y - d1 + i - 1]
                        ap[3] += line[n - 1] - line[y - d1 + 2 * d2 - i]
                        # if x == 2 and y == 4 and d1 == 2 and d2 == 1:
                        #     print(x + d1 + i)
                        #     print(ap)

                for i in range(n - 1 - x - d1 - d2):  # 3/4
                    line = acc_sum[x + d1 + d2 + 1 + i]
                    ap[2] += line[y + d2 - d1 - 1]
                    ap[3] += line[n - 1] - line[y + d2 - d1 - 1]
                    # if x == 2 and y == 4 and d1 == 2 and d2 == 1:
                    #     print(x + d1 + d2 + 1 + i)
                    #     print(ap)

                # if x == 2 and y == 4 and d1 == 2 and d2 == 1:
                #     print(ap)

                diff = max(ap) - min(ap)
                if diff < min_diff:
                    min_diff = diff

print(min_diff)
