n, k = map(int, input().split())
if n >= k:
    print(n - k)
else:
    visited = [False] * 100001
    visited[k] = True
    now = [k]
    step = 0
    while not visited[n]:
        next_step = []
        for position in now:
            minus1 = position - 1
            plus1 = position + 1
            if 0 <= minus1 <= 100000 and not visited[minus1]:
                visited[minus1] = True
                next_step.append(minus1)
            if 0 <= plus1 <= 100000 and not visited[plus1]:
                visited[plus1] = True
                next_step.append(plus1)
            if not position & 1:
                div2 = position >> 1
                if 0 <= div2 <= 100000 and not visited[div2]:
                    visited[div2] = True
                    next_step.append(div2)
        now = next_step
        step += 1
    print(step)
