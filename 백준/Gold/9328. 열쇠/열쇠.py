directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

T = int(input())
for tc in range(T):
    h, w = map(int, input().split())
    building = [input() + '*' for _ in range(h)] + ['*' * w]
    has_key = {char.upper() for char in input()}
    door_locked = {chr(num): [] for num in range(65, 91)}
    visited = [[False] * w for _ in range(h)]
    stole = 0
    q = []
    for i in range(h):
        for j in (0, w - 1):
            char = building[i][j]
            if char == '*':
                continue

            visited[i][j] = True
            if char.isalpha():
                if char.isupper():
                    if char not in has_key:
                        door_locked[char].append((i, j))
                    else:
                        q.append((i, j))
                else:
                    q.append((i, j))
                    door = char.upper()
                    if door not in has_key:
                        has_key.add(door)
                        for li, lj in door_locked[door]:
                            q.append((li, lj))
            else:
                q.append((i, j))
                if char == '$':
                    stole += 1

    for j in range(1, w - 1):
        for i in (0, h - 1):
            char = building[i][j]
            if char == '*':
                continue

            visited[i][j] = True
            if char.isalpha():
                if char.isupper():
                    if char not in has_key:
                        door_locked[char].append((i, j))
                    else:
                        q.append((i, j))
                else:
                    q.append((i, j))
                    door = char.upper()
                    if door not in has_key:
                        has_key.add(door)
                        for li, lj in door_locked[door]:
                            q.append((li, lj))
            else:
                q.append((i, j))
                if char == '$':
                    stole += 1

    while q:
        nq = []
        for ci, cj in q:
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                char = building[ni][nj]
                if char == '*' or visited[ni][nj]:
                    continue

                visited[ni][nj] = True
                if char.isalpha():
                    if char.isupper():
                        if char not in has_key:
                            door_locked[char].append((ni, nj))
                        else:
                            nq.append((ni, nj))
                    else:
                        nq.append((ni, nj))
                        door = char.upper()
                        if door not in has_key:
                            has_key.add(door)
                            for li, lj in door_locked[door]:
                                nq.append((li, lj))
                else:
                    nq.append((ni, nj))
                    if char == '$':
                        stole += 1
        q = nq

    print(stole)
