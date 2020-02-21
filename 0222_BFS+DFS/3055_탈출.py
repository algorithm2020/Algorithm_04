# s가 출발
# D가 탈출구
# 장애물 : x (돌)
# 장애물 : * (물) 시간에 따라 달라짐

from collections import deque

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(''.join(map(str, input())))
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

# water[x][y] : x,y 지점에서 물이 차는 시간
water = [[-1] * m for _ in range(n)]
# dist[x][y] : x,y 지점에 방문한 시간(분)
# -1 이면 아직 방문 안 한 것
dist = [[-1] * m for _ in range(n)]


def bfs():
    # 장애물 *(물)을 세팅하자.
    # 하는 김에 출발점, 도착점 저장해놓자.
    q = deque()
    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                q.append((i, j))
                water[i][j] = 0
            elif a[i][j] == 'S':
                start_i, start_j = i, j
            elif a[i][j] == 'D':
                end_i, end_j = i, j


    # 물이 차는 시간 (water) 구해놓기 **
    # 매 분마다 인접한 네 칸에 물이 찬다.
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if water[nx][ny] == -1 and a[nx][ny] == '.':
                q.append((nx, ny))
                water[nx][ny] = water[x][y] + 1


    #본격 탐색 시작.

    # 시작점 세팅
    q.append((start_i, start_j))
    dist[start_i][start_j] = 0

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            # 범위 넘어가면 pass
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 탈출구(D)면 종료!!!!!
            if a[nx][ny] == 'D':
                print(dist[x][y] + 1)
                return
            # 돌(X)이면 pass
            if a[nx][ny] == 'X':
                continue
            # 물이 있는 시간이면 pass
            if water[nx][ny] != -1 and water[nx][ny] <= dist[x][y] + 1:
                continue
            # 고슴도치 이동!
            if dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

    # 탈출구(D)에 안 걸리면 "KAKTUS"를 출력
    print("KAKTUS")


bfs()
