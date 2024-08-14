def z(r, c):
    if r < 2 and c < 2:
        return ((r & 1) << 1) + (c & 1)
    return (z(r >> 1, c >> 1) << 2) + ((r & 1) << 1) + (c & 1)


n, R, C = map(int, input().split())
print(z(R, C))
