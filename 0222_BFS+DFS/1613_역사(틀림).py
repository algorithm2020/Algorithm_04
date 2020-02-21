# 앞번호 출발 -> 뒷번호 도착 : -1 출력
# 뒷번호 출발 -> 앞번호 도착 : 1 출력
# 위 두 경우여도 도착 못하는 경우 : 0 출력

from _collections import deque

n, m = map(int, input().split())
history = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    x, y = map(int, input().split())
    history[x].append(y)
    #a[y].append(x)


def bfs(before, after):
    global visited

    q = deque()
    q.append(before)
    visited[before] = True

    while q:
        x = q.popleft()

        for i in history[x]:
            if not visited[i]:
                if i == after:
                    return True

                q.append(i)
                visited[i] = True

    visited = [False] * (n + 1)
    return False


s = int(input())
for _ in range(s):
    before, after = map(int, input().split())


    if bfs(before, after):
        print(-1)
        continue
    if bfs(after, before):
        print(1)
        continue
    else:
        print(0)
