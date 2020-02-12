from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 덩어리 개수 체크
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if (nx,ny) in bingsan.keys() and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True

def check():
    cnt = 0
    visited = [[False] * m for _ in range(n)]

    for x, y in bingsan.keys():
        if visited[x][y] == False:
            cnt += 1
            bfs(x,y,visited)
            if cnt >= 2:
                return cnt

    return cnt


# 첫 빙산
bingsan = {}
for i in range(n):
    for j in range(m):
        if a[i][j] != 0:
            bingsan[(i, j)] = a[i][j]
cnt = check()



# n년 후 빙산
year = 0

while True:
    # 2덩어리 이상으로 분리될 때 종료
    if cnt >= 2:
        print(year)
        break
    # 빙하가 이미 다 녹은 경우 종료
    if not bingsan:
        print("0")
        break

    # 빙하가 녹는다.
    year += 1
    for x, y in bingsan.keys():
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            elif not (nx,ny) in bingsan.keys():
                bingsan[(x,y)] -= 1
    bingsan = dict({key: value for key, value in bingsan.items() if value > 0})
    


    # 덩어리 개수 체크
    # 덩어리를 매년 체크해야되나..? 덩어리가 생길 조건이 있으면 줄일 수 있을 듯한데데
    cnt = check()
