# 또 맞은 사람에 안올라가서 재제출

# 구현, 완전탐색, 그리디 알고리즘

# 문제 조건에 대해 생각하기
# 아래 주사위가 결정되면 위 주사위의 위아랫면은 결정된다.
# 옆면은 마음대로 돌릴 수 있다. -> 즉 옆면 중 최댓값끼리만 더해서 한 옆면에 오도록 쌓을 수 있다.
# 입력 순서를 잘 봐야 한다. 0번째-5번째, 1번째-3번째, 2번째-4번째가 연결되어 있다.
# 처음에 밑면을 뭘로 둘 지 6가지 경우만 나눠서 각각 시행해 보면 된다.

import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
on_the_top = [1, 2, 3, 4, 5, 6]  # 현재까지 쌓은 주사위의 윗면
best = [0, 0, 0, 0, 0, 0]  # 현재까지 쌓은 것 중 옆면의 최대치

# 룩업 테이블 만들기

# most_except_up_and_down[i][j]는 윗면 아랫면이 i,j일때 남은 옆면 중 최댓값
# 매번 구하지 않고 룩업 테이블로 미리 만들어둔다.

# most_except_up_and_down = [[6] * 7 for _ in range(7)]
# for i in range(6):
#     most_except_up_and_down[i][6] = 5
#     most_except_up_and_down[6][i] = 5
# most_except_up_and_down[6][5] = 4
# most_except_up_and_down[5][6] = 4
# for i in range(7):
#     most_except_up_and_down[i] = tuple(most_except_up_and_down[i])
# print(tuple(most_except_up_and_down))

most_except_up_and_down = ((6, 6, 6, 6, 6, 6, 5), (6, 6, 6, 6, 6, 6, 5), (6, 6, 6, 6, 6, 6, 5), (6, 6, 6, 6, 6, 6, 5),
                           (6, 6, 6, 6, 6, 6, 5), (6, 6, 6, 6, 6, 6, 4), (5, 5, 5, 5, 5, 4, 6))

for i in range(n):
    dice = list(map(int, input().split()))
    connected = [0] * 7
    connected[dice[0]] = dice[5]
    connected[dice[1]] = dice[3]
    connected[dice[2]] = dice[4]
    connected[dice[3]] = dice[1]
    connected[dice[4]] = dice[2]
    connected[dice[5]] = dice[0]
    for idx, number in enumerate(on_the_top):  # 지금 깔으려는 주사위의 밑면 숫자 : number
        top_number = connected[number]  # 그 주사위의 윗면 숫자
        on_the_top[idx] = top_number  # 윗면(다음 주사위의 아랫면) 숫자 갱신
        best[idx] += most_except_up_and_down[number][top_number]  # number와 top_number 제외한 옆면 중 최댓값

print(max(best))
