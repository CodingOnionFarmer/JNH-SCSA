answer = list(map(int, input().split()))
for i in range(10):
    answer[i] -= 1
correct_cnt = [[1 if j == answer[i] else 0 for j in range(5)] for i in range(10)]
third_choice = [[[num for num in range(5) if not num == i == j] for j in range(5)] for i in range(5)]


def guess(idx, correct, before2, before1):
    if idx == 10:
        if correct > 4:
            return 1
        return 0
    if correct + 10 - idx < 5:
        return 0
    cnt = 0
    for choice in third_choice[before2][before1]:
        cnt += guess(idx + 1, correct + correct_cnt[idx][choice], before1, choice)
    return cnt


ans = 0
for first in range(5):
    for second in range(5):
        ans += guess(2, correct_cnt[0][first] + correct_cnt[1][second], first, second)
print(ans)
