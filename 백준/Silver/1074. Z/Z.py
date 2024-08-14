def z(r, c):
    if r < 2 and c < 2:
        return (r << 1) + c
    return (z(r >> 1, c >> 1) << 2) + z(r & 1, c & 1)


n, r, c = map(int, input().split())
print(z(r, c))
