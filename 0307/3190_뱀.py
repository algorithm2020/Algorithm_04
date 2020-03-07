# 뱀의 현재 위치를 큐에 넣는다.
# 다음 위치를 구한다
# 빈칸이면, 다음위치를 큐에 넣고 하나는 뺀다. (꼬리) 다음위치의 값을 1로 세팅한다. (뱀) 잘린 꼬리의 값은 0으로 세팅한다.
# 사과면, 다음위치를 큐에 넣는다.
# 범위가 넘었거나, 다음위치가 뱀이면 종료한다.
# 시간 +1 초
# 이동방향 변경하는 시간인지 체크하여 변경
# L : 왼->아래, 오->위, 위->왼, 아래->오
# D : 왼->위, 오->아래, 위->오, 아래->왼

from collections import deque

# 오 왼 아래 위
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0)
L = (3, 2, 0, 1)
D = (2, 3, 1, 0)


def solve():
    # 시작점
    # z=0 (방향변경지점 인덱스), d=0 (오른쪽 이동 인덱스), ans=0 (시간)
    x, y, z, d, ans = 0, 0, 0, 0, 0
    # a=0 : 빈칸, a=1 : 사과, a=2 : 뱀
    a[0][0] = 2
    q = deque()
    q.append((0, 0))

    while True:

        # 다음위치 구하고, 시간 +1초
        x, y = x + dx[d], y + dy[d]
        ans += 1

        # 다음위치가 범위를 넘어갔거나, 뱀이 있는 곳이면 종료!
        if x < 0 or x >= n or y < 0 or y >= n or a[x][y] == 2:
            print(ans)
            return

        # 다음위치가 빈칸인 경우, 원래 위치는 0으로 세팅 (꼬리잘림)
        if a[x][y] == 0:
            nx, ny = q.popleft()
            a[nx][ny] = 0

        a[x][y] = 2
        q.append((x, y))

        # 방향 바꾸는 지점 체크
        if z < m :
            t, c = b[z]  # t=시간, c=이동방향
            if ans == int(t):
                if c == 'L':
                    d = L[d]
                else:
                    d = D[d]
                z += 1


n = int(input())
a = [[0] * n for _ in range(n)]

# 사과위치
for _ in range(int(input())):
    u, v = map(int, input().split())
    a[u - 1][v - 1] = 1

# 이동방향 바뀌는 시간
m = int(input())
b = [list(map(str, input().split())) for _ in range(m)]


solve()
