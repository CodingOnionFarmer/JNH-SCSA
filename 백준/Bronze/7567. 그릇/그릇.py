dishes = input()
under = ''
ans = 5 * len(dishes)
for dish in dishes:
    if dish != under:
        ans += 5
        under = dish
print(ans)
