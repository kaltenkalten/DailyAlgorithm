class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0: return 0
        
        cumul_cost = [[0] * len(costs[0]) for i in range(len(costs))]
        
        for c in range(len(costs[0])):
            cumul_cost[0][c] = costs[0][c]
            
        for r in range(1,len(costs)):
            for c in range(len(costs[0])):
                cumul_cost[r][c] = costs[r][c] + min(cumul_cost[r-1][:c] + cumul_cost[r-1][c+1:])
                
        #print(cumul_cost)
        return min(cumul_cost[-1])
