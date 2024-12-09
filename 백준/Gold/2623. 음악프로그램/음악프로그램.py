n, m = map(int, input().split())
prior = {i + 1: set() for i in range(n)}
unlocked = {i for i in range(1, n + 1)}
for _ in range(m):
    order = list(map(int, input().split()))
    for i in range(1, order[0]):
        prior[order[i + 1]].add(order[i])
        unlocked.discard(order[i + 1])
answer = []
checked = [False] * (n + 1)
made = True
for _ in range(n):
    if not unlocked:
        made = False
        break
    singer = unlocked.pop()
    answer.append(singer)
    checked[singer] = True
    for i in range(1, n + 1):
        if not checked[i]:
            prior[i].discard(singer)
            if not prior[i]:
                unlocked.add(i)
if made:
    for singer in answer:
        print(singer)
else:
    print(0)
