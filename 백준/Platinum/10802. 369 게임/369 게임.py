a, b = input().split()
s = 0
s1 = s2 = l0 = l1 = l2 = 0
same = True
for i in range(len(a)):
    l0, l1, l2 = l0 + 3 * l1 + 3 * l2, 3 * l0 + l1 + 3 * l2, 3 * l0 + 3 * l1 + l2
    if same:
        n = ord(a[i]) - 48
        if not n % 3:
            if n == 3:
                same = False
                l0 += 1
                l1 += 1
                l2 += 1
            elif n == 6:
                same = False
                if not s:
                    l0 += 1
                    l1 += 2
                    l2 += 2
                elif s == 1:
                    l0 += 2
                    l1 += 1
                    l2 += 2
                else:
                    l0 += 2
                    l1 += 2
                    l2 += 1
            elif n == 9:
                same = False
                if not s:
                    l0 += 1
                    l1 += 3
                    l2 += 3
                elif s == 1:
                    l0 += 3
                    l1 += 1
                    l2 += 3
                else:
                    l0 += 3
                    l1 += 3
                    l2 += 1
        else:
            if n == 1:
                if not s:
                    l0 += 1
                elif s == 1:
                    l1 += 1
                else:
                    l2 += 1
            elif n == 2:
                if not s:
                    l0 += 1
                    l1 += 1
                elif s == 1:
                    l1 += 1
                    l2 += 1
                else:
                    l0 += 1
                    l2 += 1
            elif n == 4:
                if not s:
                    l0 += 1
                    l1 += 1
                    l2 += 1
                elif s == 1:
                    l0 += 1
                    l1 += 1
                    l2 += 1
                else:
                    l0 += 1
                    l1 += 1
                    l2 += 1
            elif n == 5:
                if not s:
                    l0 += 1
                    l1 += 2
                    l2 += 1
                elif s == 1:
                    l0 += 1
                    l1 += 1
                    l2 += 2
                else:
                    l0 += 2
                    l1 += 1
                    l2 += 1
            elif n == 7:
                if not s:
                    l0 += 1
                    l1 += 2
                    l2 += 2
                elif s == 1:
                    l0 += 2
                    l1 += 1
                    l2 += 2
                else:
                    l0 += 2
                    l1 += 2
                    l2 += 1
            elif n == 8:
                if not s:
                    l0 += 1
                    l1 += 3
                    l2 += 2
                elif s == 1:
                    l0 += 2
                    l1 += 1
                    l2 += 3
                else:
                    l0 += 3
                    l1 += 2
                    l2 += 1
            s = (s + n) % 3
    l0 %= 20150523
    l1 %= 20150523
    l2 %= 20150523
anum = l1 + l2
s = 0
s1 = s2 = l0 = l1 = l2 = 0
same = True
for i in range(len(b)):
    l0, l1, l2 = l0 + 3 * l1 + 3 * l2, 3 * l0 + l1 + 3 * l2, 3 * l0 + 3 * l1 + l2
    if same:
        n = ord(b[i]) - 48
        if not n % 3:
            if n == 3:
                same = False
                l0 += 1
                l1 += 1
                l2 += 1
            elif n == 6:
                same = False
                if not s:
                    l0 += 1
                    l1 += 2
                    l2 += 2
                elif s == 1:
                    l0 += 2
                    l1 += 1
                    l2 += 2
                else:
                    l0 += 2
                    l1 += 2
                    l2 += 1
            elif n == 9:
                same = False
                if not s:
                    l0 += 1
                    l1 += 3
                    l2 += 3
                elif s == 1:
                    l0 += 3
                    l1 += 1
                    l2 += 3
                else:
                    l0 += 3
                    l1 += 3
                    l2 += 1
        else:
            if n == 1:
                if not s:
                    l0 += 1
                elif s == 1:
                    l1 += 1
                else:
                    l2 += 1
            elif n == 2:
                if not s:
                    l0 += 1
                    l1 += 1
                elif s == 1:
                    l1 += 1
                    l2 += 1
                else:
                    l0 += 1
                    l2 += 1
            elif n == 4:
                if not s:
                    l0 += 1
                    l1 += 1
                    l2 += 1
                elif s == 1:
                    l0 += 1
                    l1 += 1
                    l2 += 1
                else:
                    l0 += 1
                    l1 += 1
                    l2 += 1
            elif n == 5:
                if not s:
                    l0 += 1
                    l1 += 2
                    l2 += 1
                elif s == 1:
                    l0 += 1
                    l1 += 1
                    l2 += 2
                else:
                    l0 += 2
                    l1 += 1
                    l2 += 1
            elif n == 7:
                if not s:
                    l0 += 1
                    l1 += 2
                    l2 += 2
                elif s == 1:
                    l0 += 2
                    l1 += 1
                    l2 += 2
                else:
                    l0 += 2
                    l1 += 2
                    l2 += 1
            elif n == 8:
                if not s:
                    l0 += 1
                    l1 += 3
                    l2 += 2
                elif s == 1:
                    l0 += 2
                    l1 += 1
                    l2 += 3
                else:
                    l0 += 3
                    l1 += 2
                    l2 += 1
            s = (s + n) % 3
    l0 %= 20150523
    l1 %= 20150523
    l2 %= 20150523
bnum = l1 + l2
if same and s:
    bnum += 1
print(((int(b) - int(a) + 1) - (bnum - anum)) % 20150523)
