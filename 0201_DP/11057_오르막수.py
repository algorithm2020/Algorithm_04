# d[n][k] : n자리 수에 마지막 숫자가 k인 경우
## d[n][1] = d[n-1][0] + d[n-1][1]
## d[n][2] = d[n-1][0] + d[n-1][1] + d[n-1][2]
## ...
## d[n][9] = d[n-1][0] + .. + d[n-1][9]

n = int(input())
d = [[0]*10 for _ in range(n+1)]

def dp():
    # 1자리 수에 마지막 숫자가 0~9인 경우, 오르막수의 개수 (무조건 1개씩만 있음. 1자리 수니까)
    for i in range(0, 10):
        d[1][i] = 1

    # n자리 수에 마지막 숫자가 0~9인 경우, 오르막수의 개수
    for i in range(2, n+1):
        for j in range(10):
            for k in range(j+1):
                d[i][j] += d[i-1][k]
            d[i][j] %= 10007

dp()
print(sum(d[n])%10007)

