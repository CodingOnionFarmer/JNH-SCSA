paljin = input()
if paljin == '0':
    print(0)
else:
    head = {'0': '0', '1': '1', '2': '10', '3': '11', '4': '100', '5': '101', '6': '110', '7': '111'}
    body = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
    ejin = [None] * len(paljin)
    ejin[0] = head[paljin[0]]
    for i in range(1, len(paljin)):
        ejin[i] = body[paljin[i]]
    print(''.join(ejin))
