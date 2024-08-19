game = (
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5),
    (4, 5))


def judge(depth):
    if depth == 15:
        return 1
    i, j = game[depth]
    for result in range(3):
        if score[i * 3 + result] and score[j * 3 + 2 - result]:
            score[i * 3 + result] -= 1
            score[j * 3 + 2 - result] -= 1
            if judge(depth + 1):
                return 1
            score[i * 3 + result] += 1
            score[j * 3 + 2 - result] += 1
    return 0


ans = []
for _ in range(4):
    score = list(map(int, input().split()))
    if sum(score) != 30:
        ans.append(0)
    else:
        ans.append(judge(0))
print(*ans)
