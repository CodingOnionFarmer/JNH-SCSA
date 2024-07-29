for tc in range(int(input())):
    yon, kor = 0, 0
    for _ in range(9):
        y, k = map(int, input().split())
        yon += y
        kor += k
    if yon > kor:
        print('Yonsei')
    elif yon == kor:
        print('Draw')
    else:
        print('Korea')
