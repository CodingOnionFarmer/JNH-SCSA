mushrooms = [int(input()) for _ in range(10)]
score = 0
for i in range(10):
    if abs(100 - score) >= abs(100 - score - mushrooms[i]):
        score += mushrooms[i]
    else:
        break
print(score)
