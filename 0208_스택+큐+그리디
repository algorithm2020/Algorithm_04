# 수열 idx=0 부터 시작
# 수열[0] 이 나올때까지 push
# 그다음 pop
# 수열 idx 1증가
# 수열값이 이전 수열값보다 작으면 pop, 크면 push
# ...
# 불가능한 경우는?

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

result = []
stack = []
arr_idx = 0
number = 1
stack.append(number)
result.append('+')

while arr_idx < n and number<=n:

    # 스택이 빈 경우 (push하고 바로 pop하는 경우)
    if not stack:
        number += 1
        stack.append(number)
        result.append('+')

    if stack[-1] == arr[arr_idx]:
        stack.pop()
        result.append('-')
        arr_idx += 1
    else:
        number += 1
        stack.append(number)
        result.append('+')

#결과출력
#스택에 값이 있는 경우(수열 못만드는 경우)
if stack:
    print("NO")
else:
    for i in result:
        print(i)
