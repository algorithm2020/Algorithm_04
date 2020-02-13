from collections import deque

# 12*6 뿌요뿌요
## 문자열(input())을 하나씩 끊어서 list로 저장
byby = [list(input()) for _ in range(12)]

cnt = 0
visited = {}
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


# 뿌요 아래로 쭈욱 이동
def move(x, y):
    i = x
    #아래가 '.'이 아닐때까지 쭉 이동한 후 값 변경
    while i+1 < 12 and byby[i+1][y] == '.':
        i += 1
    byby[x][y], byby[i][y] = byby[i][y], byby[x][y]
    return


# 같은색 연결되어 있는 뿌요찾기
def bfs(b):
    global cnt

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]

            if 0<=nx<12 and 0<=ny<6:
                if not (nx, ny) in visited[b]:
                    if byby[nx][ny] == b:
                        q.append((nx, ny))
                        visited[b].append((nx,ny))


    # 뿌요 터뜨리기 (4개 이상일 때)
    if len(visited[b]) >= 4:
        for i, j in visited[b]:
            byby[i][j] = '.'
        cnt += 1

    visited.pop(b)



# 시작점을 바꿔가면서 반복
q = deque()
result = 0
while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if byby[i][j] != '.' :
                b = byby[i][j]
                q.append((i, j))
                visited[b] = [(i, j)]
                bfs(b)


    # 터뜨릴 뿌요가 없으면 종료
    if cnt == 0:
        break
    # 터뜨린 경우 뿌요 아래로 쭈욱 이동
    else:
        result += 1
        for i in range(10, -1, -1):
            for j in range(6):
                if byby[i][j] != '.' and byby[i+1][j] == '.':
                    move(i, j)

print(result)
