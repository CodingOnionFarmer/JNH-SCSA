import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# meet in the middle

dslr = ' DSLR'
D = [(i << 1) % 10000 for i in range(10000)]
S = [(i - 1) % 10000 for i in range(10000)]
revS = [(i + 1) % 10000 for i in range(10000)]
L = [(i % 1000) * 10 + i // 1000 for i in range(10000)]
R = [(i % 10) * 1000 + i // 10 for i in range(10000)]


def bfs():
    vfa = [0] * 10000  # visited from a(밑에는 b)
    vfb = [0] * 10000
    before_d = [0] * 10000
    vfa[a] = -1
    vfb[b] = -1
    aq = [a]
    bq = [b]
    a_step = b_step = 0
    while True:
        a_step += 1
        naq = []
        for num in aq:
            d_num = D[num]
            if not vfa[d_num]:
                vfa[d_num] = 1
                naq.append(d_num)
                before_d[d_num] = num
            s_num = S[num]
            if not vfa[s_num]:
                vfa[s_num] = 2
                naq.append(s_num)
            l_num = L[num]
            if not vfa[l_num]:
                vfa[l_num] = 3
                naq.append(l_num)
            r_num = R[num]
            if not vfa[r_num]:
                vfa[r_num] = 4
                naq.append(r_num)
            for n_num in (d_num, s_num, l_num, r_num):
                if vfb[n_num]:
                    temp = [None] * (a_step + b_step)
                    n = n_num
                    for idx in range(a_step - 1, -1, -1):
                        order = vfa[n]
                        temp[idx] = dslr[order]
                        if order == 1:
                            n = before_d[n]
                        elif order == 2:
                            n = revS[n]
                        elif order == 3:
                            n = R[n]
                        else:
                            n = L[n]
                    n = n_num
                    for idx in range(a_step, a_step + b_step):
                        order = vfb[n]
                        temp[idx] = dslr[order]
                        if order == 1:
                            n = D[n]
                        elif order == 2:
                            n = S[n]
                        elif order == 3:
                            n = L[n]
                        else:
                            n = R[n]
                    ans.append(''.join(temp))
                    return
        aq = naq

        b_step += 1
        nbq = []
        for num in bq:
            candidates = []
            if not num & 1:
                d_num = num >> 1
                if not vfb[d_num]:
                    vfb[d_num] = 1
                    nbq.append(d_num)
                candidates.append(d_num)
                d_num += 5000
                if not vfb[d_num]:
                    vfb[d_num] = 1
                    nbq.append(d_num)
                candidates.append(d_num)
            s_num = revS[num]
            if not vfb[s_num]:
                vfb[s_num] = 2
                nbq.append(s_num)
                candidates.append(s_num)
            l_num = R[num]
            if not vfb[l_num]:
                vfb[l_num] = 3
                nbq.append(l_num)
                candidates.append(l_num)
            r_num = L[num]
            if not vfb[r_num]:
                vfb[r_num] = 4
                nbq.append(r_num)
                candidates.append(r_num)
            for n_num in candidates:
                if vfa[n_num]:
                    temp = [None] * (a_step + b_step)
                    n = n_num
                    for idx in range(a_step - 1, -1, -1):
                        order = vfa[n]
                        temp[idx] = dslr[order]
                        if order == 1:
                            n = before_d[n]
                        elif order == 2:
                            n = revS[n]
                        elif order == 3:
                            n = R[n]
                        else:
                            n = L[n]
                    n = n_num
                    for idx in range(a_step, a_step + b_step):
                        order = vfb[n]
                        temp[idx] = dslr[order]
                        if order == 1:
                            n = D[n]
                        elif order == 2:
                            n = S[n]
                        elif order == 3:
                            n = L[n]
                        else:
                            n = R[n]
                    ans.append(''.join(temp))
                    return
        bq = nbq


ans = []
T = int(input())
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    bfs()

print(*ans, sep='\n')
