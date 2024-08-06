def check(a, b, c):
    if (a ^ c) & 1:
        return 'No'
    if c > a:
        return 'No'
    if b & 1 and not a:
        return 'No'
    return 'Yes'


for tc in range(int(input())):
    print(check(*map(int, input().split())))
