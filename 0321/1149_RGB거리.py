# 참고링크 : https://hongku.tistory.com/266

# d[i][0/1/2] : i번째 집이 R/G/B 일 때 최소비용

n = int(input())
cost = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    cost.append(tmp)
d = [[0]*3 for _ in range(n)]
ans = 0

for i in range(n):
    if i == 0:
        d[i][0] = cost[i][0]
        d[i][1] = cost[i][1]
        d[i][2] = cost[i][2]
        continue

    else:
        # R
        d[i][0] = cost[i][0] + min(d[i-1][1], d[i-1][2])
        # G
        d[i][1] = cost[i][1] + min(d[i-1][0], d[i-1][2])
        # B
        d[i][2] = cost[i][2] + min(d[i - 1][0], d[i - 1][1])

ans = min(d[n-1][0], d[n-1][1], d[n-1][2])

print(ans)
