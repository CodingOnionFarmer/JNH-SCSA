n = int(input())
numbers = list(map(int, input().split()))
first = numbers[0]
odd = []
even = []
for num in sorted(numbers):
    if num & 1:
        odd.append(num)
    else:
        even.append(num)
if len(odd) != n >> 1:
    print(-1)
else:
    is_prime = [True] * 2001
    primes = []
    for num in range(2, 2001):
        if not is_prime[num]:
            continue
        primes.append(num)
        for m in range(2, 2000 // num + 1):
            is_prime[num * m] = False
    if first & 1:
        home = odd
        away = even
    else:
        home = even
        away = odd
    home.remove(first)
    n >>= 1
    n -= 1
    graph = [[] for _ in range(n)]
    for i, h in enumerate(home):
        for j, a in enumerate(away):
            if is_prime[h + a]:
                graph[i].append(j)


    def dfs(i):
        vh[i] = True
        for j in graph[i]:
            if va[j]:
                continue
            ni = away_matching[j]
            if ni == -1:
                va[j] = True
                away_matching[j] = i
                return True
            if vh[ni]:
                continue
            va[j] = True
            if dfs(ni):
                away_matching[j] = i
                return True
        return False


    answer = []
    for j, a in enumerate(away):
        if is_prime[first + a]:
            matches = 0
            home_matched = [False] * n
            away_matching = [-1] * (n + 1)
            while True:
                new_matches = 0
                vh = [False] * n
                va = [False] * (n + 1)
                va[j] = True
                for hi in range(n):
                    if home_matched[hi]:
                        continue
                    if dfs(hi):
                        new_matches += 1
                        home_matched[hi] = True
                if not new_matches:
                    break
                matches += new_matches
            if matches == n:
                answer.append(a)
    if not answer:
        answer.append(-1)
    print(*answer)
