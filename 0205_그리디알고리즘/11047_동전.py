n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))


result = 0
# 역순으로 반복수행
# 화폐 큰 것부터 사용한다. 개수를 최소로 하기 위해.
for i in a[-1:-(len(a)+1):-1]:
    if i > k:
        continue
    result += k//i
    k %= i

print(result)
