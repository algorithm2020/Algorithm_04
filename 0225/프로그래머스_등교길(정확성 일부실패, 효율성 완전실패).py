# 아래 또는 오른쪽으로만 이동한다.
# 물이 있으면 갈 수 없다.

# (m, n-1) 또는 (m-1, n) 좌표가 큐에 들어오면 종료한다.
# 그 시점에 큐의 길이가 최단경로의 개수이다.

from _collections import deque

def solution(m, n, puddles):
    answer = 0
    q = deque()
    q.append((1,1))

    # 아래 또는 오른쪽으로만 이동
    dx = [0, 1]
    dy = [1, 0]

    while q:
        x, y = q.popleft()

        if x == m and y == n-1:
            answer = len(q) + 1
            break

        for k in range(2):
            flag = False
            nx, ny = x+dx[k], y+dy[k]
            for a, b in puddles:
                if nx==a and ny==b:
                    flag = True
            if flag:
                continue

            if nx>m or ny>n:
                continue

            q.append((nx,ny))


    return answer
