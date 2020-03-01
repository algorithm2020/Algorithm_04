# 섬(덩어리)을 찾는다. (2개 이상)
    # 모든 육지를 시작점으로 하여 탐색. (방문체크)
    # 육지 값을 섬번호로 업데이트!
# 다리의 시작점은?
    # 사방에 바다가 한 개라도 있는 곳
    # 섬 찾을 때 큐에 넣기?
# 다리의 도착점은?
    # 섬이 달라지는 순간 탐색 종료!
# 다리 탐색 시
    # level을 결과에 저장
    # 결과중 최소값이 최종 결과

#참고링크 : https://rebas.kr/689
from collections import deque

n = int(input())
map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
island = 1
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
start_q = deque()
result = 10**9

def bfs_island(x, y, _island):
    # 시작점
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    map[x][y] = _island

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            #범위체크
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue

            #연결된 육지면 같은 섬이당.
            if map[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx,ny))
                visited[nx][ny] = True
                map[nx][ny] = _island

            #다리 시작점인 애들 저장
            if map[nx][ny] == 0 and not (x,y,_island) in start_q:
                start_q.append((x,y,_island))

def bfs_bridge(x,y,_island):
    visited = [[False] * n for _ in range(n)]
    level = 0
    global result

    #다리 시작점
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        size = len(q)
        level += 1

        for _ in range(size):
            x, y = q.popleft()

            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]

                # 범위체크
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                # 종료조건 (다른 섬 도착)
                if map[nx][ny] != 0 and map[nx][ny] != _island:
                    result = min(result, level-1)
                    return

                # 다리 놓자!
                if map[nx][ny] == 0 and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny] = True




# 섬 셋팅
for i in range(n):
    for j in range(n):
        #시작점
        if map[i][j] == 1 and visited[i][j] == False:
            bfs_island(i, j, island)
            island += 1


# 다리 놓기
while start_q:
    x,y,island = start_q.popleft()
    bfs_bridge(x,y,island)

print(result)
