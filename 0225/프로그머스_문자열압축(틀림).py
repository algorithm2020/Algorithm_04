# 1개, 2개, 3개 .. 단위로 반복한다.
# 단위별로 스택에 넣고 문자열과 비교한다.

def solution(s):
    answer = []
    size = len(s)

    # 문자열 자를 단위
    for i in range(1, size):
        cnt = 1
        temp_ans = []
        temp_ans.append(s[0:i])

        for j in range(i, size, i):
            flag = False
            if j+i > size:
                temp_ans.append(s[j:size])
                break
            else:
                if temp_ans[-1] == s[j:j+i]:
                    cnt += 1
                    flag = True
                else:
                    if cnt > 1:
                        temp_ans.append(str(cnt))
                        cnt = 1
                    temp_ans.append(s[j:j+i])

        if flag:
            temp_ans.append(str(cnt))
        answer.append(len(''.join(temp_ans)))

    #print(answer)
    return min(answer)
