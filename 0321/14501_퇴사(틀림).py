# d[i] : i일부터 상담을 했을 때 최대 수익
# 건너뛰는 경우 고려해야 됨 ㅠㅠ (케이스 3번)

d = {}
ans = 0
t = [0]
p = [0]
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)


def dfs(i):

    global d

    if not i in d.keys():
        if i+ t[i] <= n+1:
            d[i] = p[i]
        else:
            return

    ni = i + t[i]

    if ni <= n:
        if not ni in d.keys():
            dfs(ni)
        else:
            d[i] += d[ni]


for i in range(n, 0, -1):
    dfs(i)


print(max(d.values()))
