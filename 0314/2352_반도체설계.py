# DP
# 참고링크 : https://better-than-alone.tistory.com/89

N = int(input())
datas = list(map(int,input().split(' ')))
# subLists[i] : 포트 i에 연결했을 때 꼬이지 않는 선의 최대 개수
subLists =  [0 for i in range(N)]

for val in datas: # 포트 val에 연결하는 경우
    if (subLists[val-1] == 0) :
        subLists[val-1] = 1 
    tmp_max = subLists[val-1]
    for i in range(val): # 포트 val 보다 작은 포트들 탐색
        if (subLists[i] > 0 and val-1 > i): # 겹치지 않는 경우
            if (subLists[i] + 1 > tmp_max): 
                tmp_max = tmp_max + 1
    subLists[val-1] = tmp_max # "DP" : max값을 저장함
    
print(max(subLists))
