class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 오름차순 정렬. pop할 때 효율성을 위해.
        # 부숴진 돌은 pop
        
        
        while len(stones) >= 2:
            stones.sort()
            x = stones[-2]
            y = stones[-1]

            if x==y:
                stones.pop()
                stones.pop()
            else:
                stones[-1] = y-x
                stones.pop(-2)
            
        if stones:
            return stones[0]
        else:
            return "0"
        
