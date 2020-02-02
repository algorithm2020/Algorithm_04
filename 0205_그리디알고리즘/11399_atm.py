# 순서마다 최소 대기시간을 선택한다.

n = int(input())
atm = list(map(int, input().split()))

# 정렬하고
atm.sort()
# 더한다.
result = 0
for i in range(1, n+1):
    result += sum(atm[:i])

print(result)
