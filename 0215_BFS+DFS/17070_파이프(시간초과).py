cnt = 0
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

def garo_check(px,py,qx,qy):
    #범위체크&빈칸체크
    if qy+1 < n and house[qx][qy+1] != 1:
        return True
    else:
        return False

def sero_check(px,py,qx,qy):
    if qx+1 < n and house[qx+1][qy] != 1:
        return True
    return False

def dae_check(px,py,qx,qy):
    if qx+1 < n and qy+1 < n :
        if house[qx][qy+1] != 1 and house[qx+1][qy] != 1 and house[qx+1][qy+1] != 1:
            return True
    return False


def check(px,py,qx,qy,m):
    global cnt

    #도착했으면 종료
    if qx == n-1 and qy == n-1:
        cnt += 1
        return

    # **_check() 함수가 true일때만 check() 호출
    if m == "garo":
        if garo_check(px,py,qx,qy):
            check(px,py+1,qx,qy+1,"garo")
        if dae_check(px,py,qx,qy):
            check(px+1,py+1,qx+1,qy+1,"dae")
    elif m == "sero":
        if sero_check(px,py,qx,qy):
            check(px+1,py,qx+1,qy,"sero")
        if dae_check(px,py,qx,qy):
            check(px + 1, py + 1, qx + 1, qy + 1, "dae")
    elif m == "dae":
        if garo_check(px,py,qx,qy):
            check(px,py+1,qx,qy+1,"garo")
        if sero_check(px,py,qx,qy):
            check(px+1,py,qx+1,qy,"sero")
        if dae_check(px,py,qx,qy):
            check(px + 1, py + 1, qx + 1, qy + 1, "dae")

check(0,0,0,1,"garo")
print(cnt)
