#입력
N,M = map(int,input().split())
a=[[] for _ in range(N)]
visited=[False]*N

for _ in range(M):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)

#dfs함수 구현 (깊이가 4일 때는 무조건 return)
def dfs(cnt,node):
    global flag
    visited[node] = True
    if cnt == 4:
        flag = True
        return
    
    for i in a[node]:
        if not visited[i]:
            dfs(cnt+1,i)
            # 백트래킹
            visited[i] = False
    
flag = False
#시작점을 정점 하나씩 하여 그래프 탐색하기
for i in range(N):
    dfs(0,i)
    #시작점도 방문체크 풀어준다. 다른 시작점에서 시작했을 때 여길 방문할 수도 있으니깐.
    visited[i] = False
    if flag:
        print(1)
        break
else:
    print(0)
    
    
    
    
    
