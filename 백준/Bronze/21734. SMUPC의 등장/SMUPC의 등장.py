s = input()
for char in s:
    asc = ord(char)
    cnt = 0
    while asc:
        cnt += asc % 10
        asc //= 10
    print(char * cnt)
