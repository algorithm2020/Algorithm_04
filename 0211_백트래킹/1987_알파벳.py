# DFS & 백트래킹

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
check, ans = [False]*26, 0

# 상하좌우 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    #상하좌우 이동
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]

        #범위체크
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        #알파벳 아스키코드 출력
        c = ord(a[nx][ny]) - ord('A')
        if not check[c]:
            check[c] = True
            dfs(nx, ny, cnt+1)
            #방문체크를 풀어준다. (백트래킹)
            check[c] = False


check[ord(a[0][0])-ord('A')] = True
dfs(0, 0, 1)
print(ans)

