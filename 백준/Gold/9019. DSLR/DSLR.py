import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# meet in the middle

dslr = ' DSLR'
D = [(i << 1) % 10000 for i in range(10000)]
S = [(i - 1) % 10000 for i in range(10000)]
L = [(i % 1000) * 10 + i // 1000 for i in range(10000)]
R = [(i % 10) * 1000 + i // 10 for i in range(10000)]


def bfs():
    vfa = {}  # visited from a(밑에는 b)
    vfb = {}
    before_d = {}
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
            if d_num not in vfa:
                vfa[d_num] = 1
                before_d[d_num] = num
                naq.append(d_num)
            s_num = S[num]
            if s_num not in vfa:
                vfa[s_num] = 2
                naq.append(s_num)
            l_num = L[num]
            if l_num not in vfa:
                vfa[l_num] = 3
                naq.append(l_num)
            r_num = R[num]
            if r_num not in vfa:
                vfa[r_num] = 4
                naq.append(r_num)
            for n_num in (d_num, s_num, l_num, r_num):
                if n_num in vfb:
                    temp = [None] * (a_step + b_step)
                    n = n_num
                    for idx in range(a_step - 1, -1, -1):
                        order = vfa[n]
                        temp[idx] = dslr[order]
                        if order == 1:
                            n = before_d[n]
                        elif order == 2:
                            n = (n + 1) % 10000
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
                if d_num not in vfb:
                    vfb[d_num] = 1
                    nbq.append(d_num)
                candidates.append(d_num)
                d_num += 5000
                if d_num not in vfb:
                    vfb[d_num] = 1
                    nbq.append(d_num)
                candidates.append(d_num)
            s_num = (num + 1) % 10000
            if s_num not in vfb:
                vfb[s_num] = 2
                nbq.append(s_num)
                candidates.append(s_num)
            l_num = R[num]
            if l_num not in vfb:
                vfb[l_num] = 3
                nbq.append(l_num)
                candidates.append(l_num)
            r_num = L[num]
            if r_num not in vfb:
                vfb[r_num] = 4
                nbq.append(r_num)
                candidates.append(r_num)
            for n_num in candidates:
                if n_num in vfa:
                    temp = [None] * (a_step + b_step)
                    n = n_num
                    for idx in range(a_step - 1, -1, -1):
                        order = vfa[n]
                        temp[idx] = dslr[order]
                        if order == 1:
                            n = before_d[n]
                        elif order == 2:
                            n = (n + 1) % 10000
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


T = int(input())
ans = []
for tc in range(1, T + 1):
    a, b = map(int, input().split())
    bfs()

print(*ans, sep='\n')
