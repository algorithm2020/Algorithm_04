# 벽을 부순 횟수에 따라 정점에서 할 수 있는 것이 달라진다.
# 그러니 벽을 부순 횟수를 큐와 dist에 추가 정보로 사용해야 한다!


from collections import deque

n, m = map(int, input().split())
miro = [list(map(int, input())) for _ in range(n)]

check = [[False] * m for _ in range(n)]
# 방문한 칸 수 (-1: 방문하지 않은 것)
# ** dist[x][y][0] : 벽 부수지 않고 방문한 칸 수 / dist[x][y][1] : 벽 부수고 방문한 칸 수
dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 처음 위치
q = deque()
q.append((0, 0, 0))
check[0][0] = True
dist[0][0][0] = 1

while q:
    # z = 벽을 부순 횟수 ( 0 또는 1 )
    x, y, z = q.popleft()

    # 위, 아래, 왼, 오 이동하면서 탐색 시작
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        
        #범위체크
        if 0 <= nx < n and 0 <= ny < m:
        
            # (1) 빈칸 벽을 지나는 경우
            if miro[nx][ny] == 0 and dist[nx][ny][z] == -1:
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append((nx, ny, z))

            # (2) 벽을 부수고 지나는 경우
            if z == 0 and miro[nx][ny] == 1 and dist[nx][ny][z+1] == -1:
                dist[nx][ny][z+1] = dist[x][y][z] + 1
                q.append((nx, ny, z + 1))
                
            # 만약 이미 벽을 부쉈다면 (z=1), (1)번 if문만 실행되어 빈칸 벽을 지나는 경우만 발생한다.


# 벽을 부수고 도착했거나, 벽을 부수지 않고 도착한 경우 모두 존재한다면
if dist[n - 1][m - 1][0] != -1 and dist[n - 1][m - 1][1] != -1:
    print(min(dist[n - 1][m - 1]))

# 벽을 부수지 않고 도착한 경우라면
elif dist[n - 1][m - 1][0] != -1:
    print(dist[n - 1][m - 1][0])

# 벽을 부수고 도착한 경우라면
elif dist[n - 1][m - 1][1] != -1:
    print(dist[n - 1][m - 1][1])

# 도착점까지 도착 못한 경우
else:
    print(-1)
