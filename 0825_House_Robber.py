class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0
        
        pre_profit = []
        max_profit = 0
        
        if len(nums) > 0:
            pre_profit.append(nums[0])
            
        if len(nums) > 1:
            pre_profit.append(max(nums[0], nums[1]))
        else:
            return pre_profit[0]
        
        for num in nums[2:]:
            max_profit = max(num+pre_profit[0], pre_profit[1])
            pre_profit[0] = pre_profit[1]
            pre_profit[1] = max_profit
        
        return pre_profit[1]
        
        
        
