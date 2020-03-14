from collections import deque

n, m = map(int, input().split())
a = [list(map(str, input())) for _ in range(n)]

dist = {}
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 처음 구슬의 위치
q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 'R':
            ri, rj = i, j
        elif a[i][j] == 'B':
            bi, bj = i, j
q.append((ri, rj, bi, bj))
dist[(ri, rj, bi, bj)] = 0


def move(_x, _y, _dx, _dy, _c):
    while a[_x + _dx][_y + _dy] != '#' and a[_x][_y] != 'O':
        _x += _dx
        _y += _dy
        _c += 1
    return _x, _y, _c


def bfs():
    while q:
        rx, ry, bx, by = q.popleft()

        if dist[(rx, ry, bx, by)] >= 10:
            break

        for k in range(4):
            # 이 방향으로 갈 수 있을 때까지 쭈욱 간다.
            nrx, nry, rc = move(rx, ry, dx[k], dy[k], 0)
            nbx, nby, bc = move(bx, by, dx[k], dy[k], 0)

            # 파란구슬이 이동하려는 곳에 구멍이 있는 경우, 다른 방향으로 이동한다.
            if a[nbx][nby] == 'O':
                continue
            # 빨간구슬이 이동하려는 곳에 구멍이 있는 경우,(탈출 성공!)
            if a[nrx][nry] == 'O':
                print(dist[(rx, ry, bx, by)] + 1)
                return

            # 빨간구슬, 파란구슬이 이동한 위치가 같을 때는 (같이 못 있음)
            if nrx == nbx and nry == nby:
                # 빨간구슬이 파란구슬보다 이전에 있어야 하거나
                if rc > bc:
                    nrx, nry = nrx - dx[k], nry - dy[k]
                else:
                    nbx, nby = nbx - dx[k], nby - dy[k]

            if not (nrx, nry, nbx, nby) in dist.keys():
                q.append((nrx, nry, nbx, nby))
                dist[(nrx, nry, nbx, nby)] = dist[(rx, ry, bx, by)] + 1

    print(-1)

bfs()
