def solution(prices):
    answer = []
    n = len(prices)
    
    for i in range(n-1):
        time = 0 
        flag = True
        for j in range(i+1, n):
            #주식이 떨어진 경우
            if prices[i] > prices[j]:
                answer.append(time+1)
                flag = False
                break
            else:
                time += 1
        if flag:
            answer.append(time)
                
    answer.append(0)
    
    return answer
