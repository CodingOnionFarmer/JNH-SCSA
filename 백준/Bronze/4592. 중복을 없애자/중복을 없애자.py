while True:
    guess = list(map(int, input().split()))
    n = guess[0]
    if not n:
        break
    now = 0
    dedupe = []
    for i in range(1, n + 1):
        if guess[i] != now:
            dedupe.append(guess[i])
            now = guess[i]
    dedupe.append('$')
    print(*dedupe)
