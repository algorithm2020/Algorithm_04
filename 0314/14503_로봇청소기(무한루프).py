# 방향
    # 0 : 북, 1: 동, 2: 남, 3: 서
# 왼쪽 방향으로 회전
    # 0 -> 3, 1 -> 0, 2->1. 3->2
    # dx, dy = [0, 1, 0, -1], [-1, 0, 1 , 0]
    # d = [3, 0, 1, 2]

from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
ans = 0

# 0 : 북, 1: 동, 2: 남, 3: 서
dx, dy = [-1, 0, 1, 0], [0, 1, 0 , -1]
L = [3, 0, 1, 2]
B = [2,3,0,1]

q = deque()
q.append((r,c,d))
visited[r][c] = True
ans += 1


def cd(r,c):

    for k in range(3):
        nr, nc = r+dx[k], c+dy[k]
        if not visited[nc][nr]:
            return False

    return True


def clean():
    while q:
        r, c, d = q.popleft()


        while True:
            nr, nc = r+dx[L[d]], c+dy[L[d]] #왼쪽 방향부터 탐색
            if 0<=nr<n and 0<=nc<m:
                if not visited[nr][nc] and room[nr][nc] != 1: # 왼쪽 방향에 아직 청소하지 않은 공간이 존재 (a)
                    q.append((nr, nc, L[d]))
                    visited[nr][nc] = True
                    ans += 1
                    break
                else: # 왼쪽 방향에 청소할 공간이 없다 (b)
                    d = L[d]
                    continue # 다시 왼쪽 방향부터 탐색 (여기서 계속 무한루프)


                # 왼쪽 제외한 방향 모두 탐색
                if cd(r,c): #네 방향 모두 청소가 이미 되어있거나 벽인 경우
                    if room[r+dx[B[d]]][c+dy[B[d]]] == 1:# 후진 불가능하면 종료
                        return


clean()
print(ans)
