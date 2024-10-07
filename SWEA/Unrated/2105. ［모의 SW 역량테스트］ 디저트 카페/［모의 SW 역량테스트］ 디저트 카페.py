# 완전탐색

def solve():
    for size in range(n - 1, 1, -1):
        for left in range(1, size):
            right = size - left
            for sx in range(n - size):
                for y in range(left, n - right):
                    x = sx
                    visited = [False] * 101
                    for right_down in range(right):
                        dessert = desserts[x][y]
                        if visited[dessert]:
                            break
                        visited[dessert] = True
                        x += 1
                        y += 1
                    else:
                        for left_down in range(left):
                            dessert = desserts[x][y]
                            if visited[dessert]:
                                break
                            visited[dessert] = True
                            x += 1
                            y -= 1
                        else:
                            for left_up in range(right):
                                dessert = desserts[x][y]
                                if visited[dessert]:
                                    break
                                visited[dessert] = True
                                x -= 1
                                y -= 1
                            else:
                                for right_up in range(left):
                                    dessert = desserts[x][y]
                                    if visited[dessert]:
                                        break
                                    visited[dessert] = True
                                    x -= 1
                                    y += 1
                                else:
                                    print(f'#{tc}', size << 1)
                                    return
    print(f'#{tc}', -1)
    return


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    desserts = [list(map(int, input().split())) for _ in range(n)]
    solve()
