import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

dslr = ' DSLR'
D = [(i << 1) % 10000 for i in range(10000)]
S = [(i - 1) % 10000 for i in range(10000)]
L = [(i % 1000) * 10 + i // 1000 for i in range(10000)]
R = [(i % 10) * 1000 + i // 10 for i in range(10000)]

T = int(input())
ans = []
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    visited = [0] * 10000
    before_D = [0] * 10000
    visited[a] = -1
    q = [a]
    step = 0
    while not visited[b]:
        step += 1
        nq = []
        for num in q:
            d_num = D[num]
            if not visited[d_num]:
                visited[d_num] = 1
                nq.append(d_num)
                before_D[d_num] = num
            s_num = S[num]
            if not visited[s_num]:
                visited[s_num] = 2
                nq.append(s_num)
            l_num = L[num]
            if not visited[l_num]:
                visited[l_num] = 3
                nq.append(l_num)
            r_num = R[num]
            if not visited[r_num]:
                visited[r_num] = 4
                nq.append(r_num)
        q = nq
    temp = []
    for _ in range(step):
        order = visited[b]
        temp.append(dslr[order])
        if order == 1:
            b = before_D[b]
        elif order == 2:
            b = (b + 1) % 10000
        elif order == 3:
            b = R[b]
        else:
            b = L[b]
    ans.append(''.join(reversed(temp)))

print(*ans, sep='\n')
