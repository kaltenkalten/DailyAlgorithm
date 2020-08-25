class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0
        
        max_tmp = nums[0]
        min_tmp = nums[0]
        global_max = nums[0]
        
        for num in nums[1:]:
            max_tmp, min_tmp = max(max_tmp * num, min_tmp * num, num), min(max_tmp * num, min_tmp * num, num)
            global_max = max(global_max, max_tmp)
            #print(global_max)
        return global_max
