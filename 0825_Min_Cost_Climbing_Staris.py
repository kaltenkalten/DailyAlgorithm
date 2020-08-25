class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = [0] * len(cost)
        memo[0:2] = cost[0:2]
        
        for i in range(2,len(cost)):
            memo[i] = cost[i] + min(memo[i-1], memo[i-2])
            
        
        return min(memo[-1], memo[-2])
