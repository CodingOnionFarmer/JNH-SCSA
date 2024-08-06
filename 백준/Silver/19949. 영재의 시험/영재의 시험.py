answer = list(map(int, input().split()))
for i in range(10):
    answer[i] -= 1
correct_cnt = [[1 if j == answer[i] else 0 for j in range(5)] for i in range(10)]
# 먼저 푼 코드에서 함수를 이용해서, 5문제를 이미 맞은 경우에 대한 경우의 수를 구해 하드코딩해두었다.
already_got5_same = [0, 0, 0, 0, 0, 2240, 464, 96, 20, 4, 1]  # 마지막 2개가 같은 경우
already_got5_diff = [0, 0, 0, 0, 0, 2704, 560, 116, 24, 5, 1]  # 마지막 2개가 다른 경우
ans = 0


def guess(idx, correct, before2, before1):
    if correct + 10 - idx < 5:
        return
    if correct == 5:
        global ans
        if before2 == before1:
            ans += already_got5_same[idx]
            return
        ans += already_got5_diff[idx]
        return
    for choice in range(5):
        if before2 == before1 == choice:
            continue
        guess(idx + 1, correct + correct_cnt[idx][choice], before1, choice)
    return


guess(0, 0, -2, -1)
print(ans)
