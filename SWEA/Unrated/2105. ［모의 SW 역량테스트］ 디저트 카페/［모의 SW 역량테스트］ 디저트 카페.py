# 완전탐색

directions = ((1, 1), (1, -1), (-1, -1), (-1, 1))


def eat():
    for size in range(n - 1, 1, -1):
        for left in range(1, size):
            right = size - left
            for sx in range(n - size):
                for y in range(left, n - right):
                    x = sx
                    visited = [False] * 101
                    for d, (dx, dy) in enumerate(directions):
                        move = left if d & 1 else right
                        for _ in range(move):
                            if visited[desserts[x][y]]:
                                break
                            visited[desserts[x][y]] = True
                            x += dx
                            y += dy
                        else:
                            continue
                        break
                    else:
                        return size << 1

    return -1


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    desserts = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc} {eat()}')
