six = (
    '|',
    'b-',
    'p-|',
    '||b-',
    '|b-||',
    'b--db-'
)

nine = (
    '|',
    'b-',
    'p-|',
    '||b-',
    '-d|-q',
    'p-b-||',
    '|p-p-b-',
    '||||p-||',
    'b-b-|-db-'
)

six_square = (
    'p-p-p-',
    '||||||',
    '-d-d-d',
    'p-p-p-',
    '||||||',
    '-d-d-d'
)

six_nine_rectangle = (
    'p-p-p-',
    '||||||',
    '-d-d-d',
    'p-p-p-',
    '||||||',
    '-d-d-d',
    'p-p-p-',
    '||||||',
    '-d-d-d'
)


def mul3(number):
    stairs = [[] for _ in range(number)]
    sixes = 0
    while number > 9:
        for i, line in enumerate(six_square):
            stairs[sixes * 6 + i].append(line * sixes)
            stairs[sixes * 6 + i].append(six[i])
        sixes += 1
        number -= 6
    if number == 6:
        for i, line in enumerate(six_square):
            stairs[sixes * 6 + i].append(line * sixes)
            stairs[sixes * 6 + i].append(six[i])
    else:
        for i, line in enumerate(six_nine_rectangle):
            stairs[sixes * 6 + i].append(line * sixes)
            stairs[sixes * 6 + i].append(nine[i])
    for line in stairs:
        print(*line, sep='')


n = int(input())
re = n % 3
if not re:
    if n == 3:
        print('impossible')
    elif n == 6:
        for line in six:
            print(line)
    elif n == 9:
        for line in nine:
            print(line)
    else:
        mul3(n)
elif re == 1:
    print('impossible')
else:
    if n == 2:
        print('|')
        print('b-')
    elif n == 5:
        print('impossible')
    else:
        n -= 2
        mul3(n)
        print('p-|' * (n // 3), '|', sep='')
        print('|-d' * (n // 3), 'b-', sep='')
