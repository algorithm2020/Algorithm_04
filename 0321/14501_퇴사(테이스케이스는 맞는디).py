# 틀린 이유 : i일째 일을 건너뛰는 경우가 고려되지 않음

# d[i] : i일부터 상담을 했을 때 최대 수익


ans = 0
t = [0]
p = [0]
n = int(input())
d = [0] * (n+1)
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)


def dfs(i):

    global d

    if d[i] == 0:
        if i+ t[i] <= n+1:
            d[i] = p[i]
        else:
            return

    ni = i + t[i]

    if ni <= n:
        if d[i] == 0:
            dfs(ni)
        elif d[ni] != 0:
            d[i] += max(d[ni:])






for i in range(n, 0, -1):

    dfs(i)


print(max(d))
