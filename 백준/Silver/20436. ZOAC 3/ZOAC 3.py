# Dynamic Programming -> 이 아니었다.
# 구현

# BOJ 경찰차 문제와 매우 유사한 문제 (경찰차가 사이즈가 훨씬 크다) -> 가 아니었다.

# 룩업 테이블 만들기
# 키보드에서 각 키의 위치를 룩업 테이블로 만들었다.
# 룩업 테이블을 만드는 코드를 생략하고, 결과물을 콘솔에 출력한 뒤
# 복사해서 하드코딩으로 만들어서 쓰면 성능이 더 향상된다.


# !!!틀렸던 이유!!!
# 자음은 왼손, 모음은 오른손이라는 조건이 있네요.....


# keyboard = {}
# for i, ch in enumerate('qwertyuiop'):
#     keyboard[ch] = (0, i)
# for i, ch in enumerate('asdfghjkl'):
#     keyboard[ch] = (1, i)
# for i, ch in enumerate('zxcvbnm'):
#     keyboard[ch] = (2, i)
#
# print(keyboard)

keyboard = {'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7),
            'o': (0, 8), 'p': (0, 9), 'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5),
            'j': (1, 6), 'k': (1, 7), 'l': (1, 8), 'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4),
            'n': (2, 5), 'm': (2, 6)}

# left = set()
# for ch in 'qwertasdfgzxcv':
#     left.add(ch)
# print(left)

left = {'a', 'w', 'g', 'q', 'e', 'v', 'c', 'r', 't', 'd', 'z', 's', 'f', 'x'}

sl, sr = input().split()
cli, clj = keyboard[sl]
cri, crj = keyboard[sr]
word = input()
ans = len(word)
for ch in word:
    ni, nj = keyboard[ch]
    if ch in left:
        ans += abs(cli - ni)
        ans += abs(clj - nj)
        cli = ni
        clj = nj
    else:
        ans += abs(cri - ni)
        ans += abs(crj - nj)
        cri = ni
        crj = nj
print(ans)
