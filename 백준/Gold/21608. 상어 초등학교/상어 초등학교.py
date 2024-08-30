"""
BOJ : 상어 초등학교

시작 시간 : 9시 07분
구상 완료 : 9시 09분
1회 오답 : 9시 41분
제출 시간 : 9시 49분

"""

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n = int(input())
adj = [[(i + di) * n + j + dj for di, dj in directions if 0 <= i + di < n and 0 <= j + dj < n] for i in range(n) for j
       in range(n)]
sit = [0] * (n ** 2)
student_sit = [-1] * (n ** 2 + 1)
adj_empty = [len(adj[idx]) for idx in range(n ** 2)]
students_and_favorites = [list(map(int, input().split())) for _ in range(n ** 2)]

for idx in range(n ** 2):
    student = students_and_favorites[idx][0]
    favorites_adj = {}
    for j in range(1, 5):
        favorite = students_and_favorites[idx][j]
        if student_sit[favorite] < 0:
            continue
        for adj_sit in adj[student_sit[favorite]]:
            if sit[adj_sit]:
                continue
            if adj_sit in favorites_adj:
                favorites_adj[adj_sit] += 1
            else:
                favorites_adj[adj_sit] = 1

    # print(student)
    # print(favorites_adj)

    if favorites_adj:
        best_sit = -sorted([(fa, adj_empty[s], -s) for s, fa in favorites_adj.items()], reverse=True)[0][2]
    else:
        best_sit = 0
        most_empty = -1
        for sit_idx in range(n ** 2):
            if sit[sit_idx]:
                continue
            if adj_empty[sit_idx] > most_empty:
                best_sit = sit_idx
                most_empty = adj_empty[sit_idx]
                if most_empty == 4:
                    break
    # print(best_sit)
    # print('-------------------')
    student_sit[student] = best_sit
    sit[best_sit] = student
    for adj_sit in adj[best_sit]:
        adj_empty[adj_sit] -= 1

# print(adj_empty)
# print(sit)

ans = 0
score = (0, 1, 10, 100, 1000)
for idx in range(n ** 2):
    student = students_and_favorites[idx][0]
    ss = student_sit[student]
    favorite_cnt = 0
    for sas in adj[ss]:
        adj_student = sit[sas]
        if adj_student in students_and_favorites[idx]:
            favorite_cnt += 1
    ans += score[favorite_cnt]

print(ans)
