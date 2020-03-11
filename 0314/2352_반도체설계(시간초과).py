# 모든 조합 (n개, n-1개, .. 1개 선택)
    # 겹치는 순간 skip
        # 이전 값보다 지금 값이 작은 경우
    # 안 겹치면 뽑은 개수 출력

from itertools import combinations

n = int(input())
port = list(map(int, input().split()))
c = list(range(n))

def solution():
    for k in range(n, 0, -1): #조합 몇 개 뽑을지
        for i in combinations(c, k): # i : 튜플 형태로 출력됨
            flag = True
            for j in range(1, k):

                if port[i[j-1]] > port[i[j]]: # 선이 겹치는 경우 (이전 값보다 지금 값이 작은 경우)
                    flag = False
                    break
            if flag: # break 빠져나오는 단계.
                print(k)
                return


solution()
