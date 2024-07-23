h, w = map(int, input().split())
for i in range(h):
    now = input()
    forecast = [0] * w
    cloud = False
    for j in range(w):
        if now[j] == 'c':
            cloud = True
            distance = 0
        else:
            if not cloud:
                forecast[j] = -1
            else:
                distance += 1
                forecast[j] = distance
    print(*forecast)
