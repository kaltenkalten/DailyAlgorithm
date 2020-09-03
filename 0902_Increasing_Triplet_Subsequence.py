class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:  return False
        i = nums[0]
        j = float('inf')
        
        for num in nums[1:]:
            if i < num:
                j = min(j, num)
                if j < num:
                    return True
            else:
                i = num
                
        return False
