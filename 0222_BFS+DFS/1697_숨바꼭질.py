from collections import deque

n, k = map(int, input().split())
max_int = 1000000
check = [False] * max_int
dist = [-1] * max_int

# 시작점 세팅
q = deque()
q.append(n)
check[n] = True
# 걸리는 시간(초)
dist[n] = 0


while q:
    x = q.popleft()
    
    
    #범위체크 하고 방문체크 하고
    if x - 1 >= 0:
        if check[x - 1] == False:
            q.append(x - 1)
            check[x - 1] = True
            dist[x - 1] = dist[x] + 1
    if x + 1 < max_int:
        if check[x + 1] == False:
            q.append(x + 1)
            check[x + 1] = True
            dist[x + 1] = dist[x] + 1
    if 2 * x < max_int:
        if check[2 * x] == False:
            q.append(2 * x)
            check[2 * x] = True
            dist[2 * x] = dist[x] + 1

print(dist[k])
