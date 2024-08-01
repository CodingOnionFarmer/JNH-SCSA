w, n = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
double_weights = [[] for _ in range(w - 2)]
for i in range(n - 1):
    for j in range(i + 1, n):
        s = weights[i] + weights[j]
        if s < w - 2:
            double_weights[s].append(weights[i])
ans = 'NO'


def check():
    for dw in range(max(3, w - 399999), w // 2):
        rev = w - dw
        if double_weights[dw] and double_weights[rev]:
            for a in range(len(double_weights[dw])):
                for b in range(len(double_weights[rev])):
                    w1 = double_weights[dw][a]
                    w2 = double_weights[rev][b]
                    if len({w1, dw - w1, w2, rev - w2}) == 4:
                        return True
    return False


if check():
    ans = 'YES'
if not w & 1:
    if len(double_weights[w // 2]) > 1:
        ans = 'YES'
print(ans)
