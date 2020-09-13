class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #if len(nums) == 0:  return [[]]
        
        result = [[]]
        
        for num in nums:
            tmp_result = result[:]
            for tmp in tmp_result:
                result.append(tmp + [num])
                
        return result
