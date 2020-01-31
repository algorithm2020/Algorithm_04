n = int(input())
a = list(map(int, input().split()))

# d[i] : i번째에서 가장 긴 부분 수열 개수
d = [0]*n


for i in range(n):
    min_v = 0
    for j in range(i):
        # i번째 수가 더 큰 경우, 작은 수(j번째) 경우에서 구한 값을 사용한다.
        if a[j] < a[i]:
            min_v = max(min_v, d[j])
    # i번째 수도 포함되므로 +1을 해준다.        
    d[i] = min_v + 1

print(max(d))
