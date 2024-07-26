n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
ans = 3
for i, card in enumerate(cards[:n - 2]):
    p = i + 1
    q = n - 1
    if card + cards[p] + cards[p + 1] > m:
        break
    while p < q:
        three_cards = card + cards[p] + cards[q]
        if three_cards > m:
            q -= 1
        else:
            if three_cards > ans:
                ans = three_cards
            if card + cards[p + 1] + cards[q] <= m:
                p += 1
            else:
                q -= 1
print(ans)
