for tc in range(int(input())):
    print(2015 - sum(ord(char) for char in set(input())))