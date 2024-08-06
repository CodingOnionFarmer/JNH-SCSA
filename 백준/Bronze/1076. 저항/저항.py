resist = {'black': 0,
          'brown': 1,
          'red': 2,
          'orange': 3,
          'yellow': 4,
          'green': 5,
          'blue': 6,
          'violet': 7,
          'grey': 8,
          'white': 9}

ans = 0
color = input()
ans += resist[color]
ans *= 10
color = input()
ans += resist[color]
color = input()
ans *= 10 ** resist[color]
print(ans)
