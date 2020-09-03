class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        [-1, 0, 1, 2, -1, -4]
        [-4, -1, -1, 0, 1, 2]
        
        nlogn
        +
        n^2
        
        """
        if len(nums) == 0:  return []
        
        answer = []
        
        nums.sort()
        
        for idx, first in enumerate(nums[:-2]):
            if idx is not 0 and nums[idx-1] == first:
                continue
            l = idx + 1
            r = len(nums)-1
            
            while l < r:
                #print(l, r)
                Sum3 = first + nums[l] + nums[r]
                if Sum3 == 0:
                    #if [first, nums[l], nums[r]] not in answer:
                    answer.append([first, nums[l], nums[r]])
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    r -= 1
                    l += 1
                elif Sum3 > 0:
                    r -= 1
                else:
                    l += 1
                    
        return answer
                
                
                
                
                
