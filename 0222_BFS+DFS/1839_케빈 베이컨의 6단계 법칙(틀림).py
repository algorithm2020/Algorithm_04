
n, m = map(int, input().split())
friend=[[] for _ in range(n+1)]
visited = ["False"]*(n+1)


for _ in range(m):
    x, y = map(int, input().split())
    friend[x].append(y)
    friend[y].append(x)

result = [0]*(n+1)
a = [*range(1,n+1)]


def dfs(idx, start, target, cnt):
    # 찾고자 하는 친구에 도착했을 때 종료.
     # 도착하는 경로가 여러 개일 수도 있다. 그 중에서 최소 경로만 고려해야 한다.
    # 모든 사람은 친구로 이어져 있기 때문에 인덱스 범위체크는 필요 없다.

    global t

    if idx == target:
        t = min(t, cnt)
        return


    for i in friend[idx]:
        if visited[i] == "False":
            visited[i] = "True"
            dfs(i, start, target, cnt+1)

            # 1->4 일 때
                # 1->3->4 : 이 경로가 먼저 고려됨
                # 1->4 : 이 경로고 고려되어야 하기 때문에 방문체크를 풀어준다.
            visited[i] = "False"




#1번 유저부터 케빈 베이컨 계산하기
for i in range(1, n+1):

    tmp = list(map(str, a))
    tmp = ''.join(tmp)
    tmp = tmp.replace(str(i), "")

    for j in tmp:
        j = int(j)
        visited[i] = "True"
        t = n
        dfs(i, i, j, 0)
        result[i] += t

        #visited 초기화
        visited = ["False"] * (n + 1)


print(result.index(min(result[1:])))
