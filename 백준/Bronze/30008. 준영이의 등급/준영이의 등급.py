n, k = map(int, input().split())
grades = [0,4,11,23,40,60,77,89,96,100]
ranks = list(map(int, input().split()))
answer = []
for r in ranks:
    p = (r*100)//n
    for g in range(1,10):
        if p <= grades[g]:
            answer.append(g)
            break
print(*answer)
