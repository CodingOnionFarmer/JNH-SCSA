shape = {'CIRCLE': 1, 'TRIANGLE': 2, 'SQUARE': 3}
color = {'YELLOW': 1, 'RED': 2, 'BLUE': 3}
background_color = {'GRAY': 1, 'WHITE': 2, 'BLACK': 3}
HAP = {1, 6, 8, 27}

cards = []
for i in range(9):
    s, c, b = input().split()
    cards.append((shape[s], color[c], background_color[b]))

three_cards_HAP = [[[False] * 9 for _ in range(9)] for __ in range(9)]
remain_HAP = 0
for card1 in range(7):
    s1, c1, b1 = cards[card1]
    for card2 in range(card1 + 1, 8):
        s2, c2, b2 = cards[card2]
        for card3 in range(card2 + 1, 9):
            s3, c3, b3 = cards[card3]
            if s1 * s2 * s3 in HAP and c1 * c2 * c3 in HAP and b1 * b2 * b3 in HAP:
                three_cards_HAP[card1][card2][card3] = True
                remain_HAP += 1

n = int(input())
score = 0
gyul = False
for i in range(n):
    order = list(input().split())
    if order[0] == 'G':
        if remain_HAP or gyul:
            score -= 1
        else:
            score += 3
            gyul = True
    else:
        a, b, c = sorted([int(order[1]) - 1, int(order[2]) - 1, int(order[3]) - 1])
        if three_cards_HAP[a][b][c]:
            score += 1
            remain_HAP -= 1
            three_cards_HAP[a][b][c] = False
        else:
            score -= 1
print(score)
