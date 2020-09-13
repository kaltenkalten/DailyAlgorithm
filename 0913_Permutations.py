class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Combination은 어떻게 할지 생각해봐요
        if len(nums) == 0:  return []
        self.result = []
        
        def backtracking(rest_nums, cur_list):
            if len(rest_nums) == 0:
                self.result.append(cur_list)
                return
            
            for idx, num in enumerate(rest_nums):
                backtracking(rest_nums[:idx] + rest_nums[idx+1:], cur_list+[num])
                
                
        backtracking(nums, [])
        
        return self.result
