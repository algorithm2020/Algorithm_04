# 1개, 2개, 3개 .. 단위로 반복한다.
# 단위별로 스택에 넣고 문자열과 비교한다.

def solution(s):
    answer = []
    size = len(s)

    # 문자열 자를 단위
    for i in range(1, size+1):
        cnt = 1
        temp_ans = []
        temp_ans.append(s[0:i])

        for j in range(i, size, i):
            #자를 단위가 문자열 범위를 넘어가면 종료!
            if j+i > size:
                temp_ans.append(s[j:size])
                break
            else:
                #같은 문자가 있는 경우 cnt ++
                if temp_ans[-1] == s[j:j+i]:
                    cnt += 1
                #같은 문자가 아니면 스택에 넣고 cnt는 다시 초기화.
                else:
                    if cnt > 1:
                        temp_ans.append(str(cnt))
                        cnt = 1
                    temp_ans.append(s[j:j+i])

        #범위 넘어서기 전에 문자열이 반복됐으면 cnt 마저 추가해주기.
        if cnt > 1:
            temp_ans.append(str(cnt))
        answer.append(len(''.join(temp_ans)))

    #print(answer)
    return min(answer)
