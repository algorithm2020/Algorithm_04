# 6개 중에 4개를 선택한다.
# 최소 모음 1개, 자음 2개가 있다.
# 오름차순이다.
# 중복 없다.

from itertools import combinations

l, c = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()
mo = ['a', 'e', 'i', 'o', 'u']

def check_mo(a):
    result = 0
    for i in mo:
        result += a.count(i)
    return result

for c in combinations(alpha, l):
    # 자음,모음개수 체크 (l - 모음개수 >= 2, 모음개수 > 0)
    if l-2 >= check_mo(c) > 0:
        for i in c:
            print(i, end='')
        print()
