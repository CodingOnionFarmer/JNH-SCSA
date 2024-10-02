n, k = map(int, input().split())
if n >= k:
    print(n - k)
else:
    visited = [False] * 100001
    q = []
    while True:
        visited[k] = True
        q.append(k)
        if k & 1:
            break
        k >>= 1
    step = 0
    while not visited[n]:
        step += 1
        nq = []
        for cp in q:
            np = cp - 1
            if np != -1:
                while True:
                    if visited[np]:
                        break
                    visited[np] = True
                    nq.append(np)
                    if np & 1:
                        break
                    np >>= 1

            np = cp + 1
            if np != 100001:
                while True:
                    if visited[np]:
                        break
                    visited[np] = True
                    nq.append(np)
                    if np & 1:
                        break
                    np >>= 1
        q = nq
    print(step)
