n, u, l = map(int, input().split())
if n < 1000:
    print('Bad')
else:
    if u >= 8000 or l >= 260:
        print('Very Good')
    else:
        print('Good')
