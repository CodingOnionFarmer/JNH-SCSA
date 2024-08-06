answer = list(map(int, input().split()))
correct_cnt = [[1 if j == answer[i] else 0 for j in range(6)] for i in range(10)]


def guess(idx, correct, before2, before1):
    if idx == 10:
        if correct > 4:
            return 1
        return 0
    if correct + 10 - idx < 5:
        return 0
    if before1 == before2:
        return sum(guess(idx + 1, correct + correct_cnt[idx][choose], before1, choose) for choose in range(1, 6) if
                   choose != before1)
    return sum(guess(idx + 1, correct + correct_cnt[idx][choose], before1, choose) for choose in range(1, 6))


print(guess(0, 0, 0, -1))
