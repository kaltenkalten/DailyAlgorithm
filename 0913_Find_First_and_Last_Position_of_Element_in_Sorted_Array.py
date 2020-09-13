class Solution:
    def find_elements(self, nums, target):
        first = len(nums)
        l, r = 0, len(nums)-1        
        while l <= r:
            m = (l+r)//2
            if target > nums[m]:
                l = m + 1
            else:
                first = m
                r = m - 1
        return first
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.find_elements(nums, target)
        right = self.find_elements(nums, target+1) - 1
        
        if left <= right:
            return [left, right]
        else:
            return [-1,-1]
