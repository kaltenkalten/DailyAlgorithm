class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer1 = pointer2 = 0
        
        while pointer2 < len(nums):
            if nums[pointer2] < 1:
                nums[pointer2], nums[pointer1] = nums[pointer1], nums[pointer2]
                pointer1 += 1
            pointer2 += 1
        pointer1 = pointer2 = len(nums)-1
        
        while pointer2 >= 0:
            if nums[pointer2] > 1:
                nums[pointer2], nums[pointer1] = nums[pointer1], nums[pointer2]
                pointer1 -= 1
            pointer2 -= 1
        
