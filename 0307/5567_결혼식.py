# a=1 이면 (시작점)
    # b를 큐에 넣는다. (상근이의 친구)
    # 방문체크를 한다. (결혼식 초대)
    # 결과값을 +1 한다.
# 큐에서 하나씩 빼면서
# a를 키값으로 하는 딕셔너리를 사용하자.
    # friend = {1:[2,3], 2:[4]}


from collections import deque

n = int(input())
m = int(input())

friend = {}
for i in range(1, n+1):
    friend[i] = []

for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

visited = []
for _ in range(n+1):
    visited.append(False)


ans = 0
q = deque()
# 상근이의 친구
visited[1] = True
for i in friend[1]:
    q.append(i)
    visited[i] = True
    ans += 1

while q:
    temp = q.popleft()

    # 상근이 친구의 친구
    for i in friend[temp]:
        if not visited[i]: #방문하지 않았으면
            visited[i] = True
            ans += 1


print(ans)
