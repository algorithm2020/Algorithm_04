# (x,y)칸 까지의 경로수 = (x-1,y)칸 까지의 경로수 + (x,y-1)칸 까지의 경로수
# 물 웅덩이는 지나가지 못한다.


def solution(m, n, puddles):
    answer = 0

    # 모서리가 웅덩이인 경우를 고려해야 됨!
    check = [[1]*m for _ in range(n)]

    for x, y in puddles:
        check[y-1][x-1] = 0
        if x==1 and y<n:
            check[y][x-1] = 0


    for i in range(1,n):
        for j in range(1,m):
            if check[i][j] == 0:
                continue
            check[i][j] = (check[i][j-1] + check[i-1][j])%1000000007

    answer = check[n-1][m-1]
    return answer

