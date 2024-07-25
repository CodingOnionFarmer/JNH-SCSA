A = input()
B = input()
ffB = [0] * len(B)  # failure function of B
same_checked = 0
for i in range(1, len(B)):
    while same_checked and B[i] != B[same_checked]:
        same_checked = ffB[same_checked - 1]
    if B[i] == B[same_checked]:
        same_checked += 1
        ffB[i] = same_checked
checkedB = 0
seeing = 0
AB_same_length = 0
whereisB = []
while seeing < len(A):
    if A[seeing] == B[AB_same_length]:
        AB_same_length += 1
        seeing += 1
        if AB_same_length == len(B):
            checkedB += 1
            AB_same_length = ffB[AB_same_length - 1]
            whereisB.append(seeing - len(B) + 1)
    else:
        if AB_same_length:
            AB_same_length = ffB[AB_same_length - 1]
        else:
            seeing += 1
print(checkedB)
print(*whereisB)
