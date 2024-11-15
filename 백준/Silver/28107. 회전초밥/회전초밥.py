import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
sushi_queue = [[] for _ in range(200001)]
# 입력이 손님 번호 순(우선순위 순)으로 들어오므로 heapify 할 필요 없이 index순으로 줘도 된다.
parameter = [0] * 200001
# parameter[s]는 s번 초밥을 지금까지 몇 명에게 줬는지이다.
# 즉, sushi_queue[s]에서 index 몇 번째 사람에게 초밥을 줘야 하는지와 같다.
ans = [0] * n
for i in range(n):
    order = list(map(int, input().split()))
    for j in range(1, order[0] + 1):
        sushi_queue[order[j]].append(i)
given = list(map(int, input().split()))
for sushi in given:
    if len(sushi_queue[sushi]) > parameter[sushi]:
        ans[sushi_queue[sushi][parameter[sushi]]] += 1
        parameter[sushi] += 1
print(*ans)
