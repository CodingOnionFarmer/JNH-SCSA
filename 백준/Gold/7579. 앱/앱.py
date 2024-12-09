n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
check = {0}
secured = [0] * 10001
for i in range(n):
    new = set()
    for c in sorted(list(check), reverse=True):
        secured[c + cost[i]] = max(secured[c + cost[i]], secured[c] + memory[i])
        new.add(c + cost[i])
    check |= new
for i in range(10001):
    if secured[i] >= m:
        answer = i
        break
print(answer)
