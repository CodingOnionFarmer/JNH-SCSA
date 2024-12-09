n = int(input())
cards = list(map(int, input().split()))
cards_dict = {}
for card in cards:
    cards_dict[card] = 0
for i in range(1, 1000001):
    if i in cards_dict:
        k = 2 * i
        while k < 1000001:
            if k in cards_dict:
                cards_dict[i] += 1
                cards_dict[k] -= 1
            k += i
for card in cards:
    print(cards_dict[card], end=' ')
