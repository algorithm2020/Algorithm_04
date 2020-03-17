# 참고링크 : https://songsunbi.tistory.com/80

# d[i] : i일부터 상담을 했을 때 최대 수익 (i일에 건너뛸 수도 있음)


ans = 0
t = [0]
p = [0]
n = int(input())
d = [0] * (n+2)
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)


for i in range(n, 0, -1):

    next = i + t[i]
    if next > n+1: # i일에 일을 어차피 할 수 없거나
        d[i] = d[i+1]
    else:
        # i일에 일을 하는 경우와 i일을 건너 뛰는 경우 비교!
        d[i] = max(p[i]+d[next], d[i+1])

print(max(d))
