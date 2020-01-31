d = []
for _ in range(1001):
    d.append(0)

def dp(n):
    if n==1 : return 1
    if n==2 : return 2

    # 이미 구한 값은 가져다 사용한다.
    if d[n] != 0 : return d[n]

    #점화식
    d[n] = (dp(n-1) + dp(n-2)) % 10007
    return d[n]

num = int(input())
print(dp(num))

