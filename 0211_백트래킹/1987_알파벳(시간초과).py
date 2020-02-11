#BFS로 품. (시간초과)
#상하좌우 모두 탐색후에 알파벳 방문체크를 한다.

# 상하좌우 이동
# 이미 지나온 알파벳은 갈 수 없다.
# 말이 지날 수 있는 최대의 칸 수

from collections import deque

n, m = map(int, input().split())
alpha = [[]*m for _ in range(n)]
for i in range(n):
    a = input()
    alpha[i] = list(a)

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
check = []
temp_check = []
result = 0

#처음위치 (좌측상단부터 시작)
q = deque()
q.append((0,0))
check.append(alpha[0][0])



while q:
    q_size = len(q)

    for _ in range(q_size):
        x, y = q.popleft()
        #print(alpha[x][y])

        #상하좌우 이동
        for k in range(4):
            temp_check = []
            nx, ny = x+dx[k], y+dy[k]

            #범위체크
            if 0<=nx<n and 0<=ny<m:
                #이미 방문한 알파벳이면 건너뛴다.
                if alpha[nx][ny] in check:
                    continue
                else:
                    q.append((nx, ny))
                    temp_check.append(alpha[nx][ny])
        check.extend(set(temp_check))
    result += 1

print(result)
