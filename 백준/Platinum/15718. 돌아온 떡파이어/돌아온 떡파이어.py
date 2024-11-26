import sys

t = int(input())
pas97 = {}
for i in range(97):
    pas97[(i, 0)] = 1
    pas97[(i, i)] = 1
for i in range(1, 96):
    for j in range(1, i + 1):
        pas97[(i + 1, j)] = (pas97[(i, j - 1)] + pas97[(i, j)]) % 97
pas1031 = {}
for i in range(1031):
    pas1031[(i, 0)] = 1
    pas1031[(i, i)] = 1
for i in range(1, 1031):
    for j in range(1, i + 1):
        pas1031[(i + 1, j)] = (pas1031[(i, j - 1)] + pas1031[(i, j)]) % 1031


def nk97(n, k):
    n1 = n // 97
    k1 = k // 97
    n %= 97
    k %= 97
    if k > n:
        return 0
    else:
        if n1 < 97 and k1 < 97:
            if k1 > n1:
                return 0
            else:
                return pas97[(n, k)] * pas97[(n1, k1)] % 97
        else:
            return pas97[(n, k)] * nk97(n1, k1) % 97


def nk1031(n, k):
    n1 = n // 1031
    k1 = k // 1031
    n %= 1031
    k %= 1031
    if k > n:
        return 0
    else:
        if n1 < 1031 and k1 < 1031:
            if k1 > n1:
                return 0
            else:
                return pas1031[(n, k)] * pas1031[(n1, k1)] % 1031
        else:
            return pas1031[(n, k)] * nk1031(n1, k1) % 1031


for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    if not m-1:
        if n:
            print(0)
        else:
            print(1)
    else:
        if not n:
            print(0)
        else:
            k97 = nk97(n - 1, m - 2)
            k1031 = nk1031(n - 1, m - 2)
            for i in range(97):
                if (i * 1031 + k1031) % 97 == k97:
                    print(i * 1031 + k1031)
                    break
