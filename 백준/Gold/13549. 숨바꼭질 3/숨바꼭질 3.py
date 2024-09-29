n, k = map(int, input().split())
if n >= k:
    print(n - k)
else:
    visited = [False] * 100001
    q = []
    while n <= 100000:
        if visited[n]:
            break
        visited[n] = True
        q.append(n)
        n <<= 1
    step = 0
    while not visited[k]:
        step += 1
        nq = []
        for cp in q:
            np = cp - 1
            if np != -1:
                while np <= 100000:
                    if visited[np]:
                        break
                    visited[np] = True
                    nq.append(np)
                    np <<= 1
                    
            np = cp + 1
            while np <= 100000:
                if visited[np]:
                    break
                visited[np] = True
                nq.append(np)
                np <<= 1
        q = nq
    print(step)
