from collections import deque

n, m = map(int, input().split())
friend=[[] for _ in range(n+1)]
visited = [False]*(n+1)


for _ in range(m):
    x, y = map(int, input().split())
    friend[x].append(y)
    friend[y].append(x)

result = [0]*(n+1)
a = [*range(1,n+1)]


def bfs(start, target):
    #시작점 세팅
    q = deque()
    q.append(start)
    visited[start] = True
    level = 0

    while q:
        s = len(q)
        level += 1
        for _ in range(s):
            idx = q.popleft()

            for k in friend[idx]:
                if not visited[k]:
                    # 찾으려는 친구에 도달했으면 탐색을 종료한다.
                    if k == target:
                        result[start] += level
                        return
                    q.append(k)
                    visited[k] = True





#1번 유저부터 케빈 베이컨 계산하기
for i in range(1, n+1):

    tmp = list(map(str, a))
    tmp = ''.join(tmp)
    tmp = tmp.replace(str(i), "")

    for j in tmp:
        j = int(j)
        bfs(i, j)

        #visited 초기화
        visited = [False] * (n + 1)

print(result.index(min(result[1:])))
