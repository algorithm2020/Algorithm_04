from itertools import combinations

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # A 고른 개수 = B 고른 개수 이어야 한다.
        
        # 브루트포스로 하려면
        # 3개 인덱스로 이루어진 조합 2개를 만들고 각각 더한다.
        # 두 개의 합이 최소인 것을 구한다.
        
               
        result = []
        n = len(costs)
        s = []
        for i in range(0, n):
            s.append(i)
        s = set(s)
        
        
        for i in combinations(s, n//2):
    
            temp_s = s - set(i)
        
            temp_result = 0       
            # a 선택 / b 선택
            for j in i:
                temp_result += costs[j][0]
            for j in temp_s:
                temp_result += costs[j][1]
            result.append(temp_result)
            
                
            temp_result = 0     
            # b 선택 / a 선택
            for j in i:
                temp_result += costs[j][1]
            for j in temp_s:
                temp_result += costs[j][0]            
            result.append(temp_result)
        
        return min(result)
        
        
         #그리디 적용하려면 경우의수 쳐낼 수 있는 조건을 찾아보자.
