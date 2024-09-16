n, k = map(int, input().split())

reach_odd = [False] * 500001
reach_even = [False] * 500001
reach_even[n] = True
q = [n]
step = 0
while k + step + 1 < 500001:
    if step & 1:
        if reach_odd[k]:
            break
    elif reach_even[k]:
        break

    step += 1
    k += step
    nq = []

    if step & 1:
        for pos in q:
            for adj in (pos + 1, pos - 1, pos << 1):
                if 0 <= adj <= 500000 and not reach_odd[adj]:
                    reach_odd[adj] = True
                    nq.append(adj)
    else:
        for pos in q:
            for adj in (pos + 1, pos - 1, pos << 1):
                if 0 <= adj <= 500000 and not reach_even[adj]:
                    reach_even[adj] = True
                    nq.append(adj)
    q = nq

if step & 1 and not reach_odd[k] or not step & 1 and not reach_even[k]:
    print(-1)
else:
    print(step)
