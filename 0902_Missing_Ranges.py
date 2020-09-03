class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        answer = []
        # [0, 1, 3, 50], upper = 10 -> ["4~10"]
        # lower = 5, [0,1,2,7]
        new_nums = [lower-1]
        
        for idx, val in enumerate(nums):
            if lower <= val <= upper:
                new_nums.append(val)
                
        new_nums.append(upper+1)
                
        for idx, val in enumerate(new_nums[:-1]):
            if (new_nums[idx] == new_nums[idx+1]) or (new_nums[idx]+1 == new_nums[idx+1]):
                continue
            if new_nums[idx+1] - new_nums[idx] == 2:
                answer.append(str(new_nums[idx]+1))
            else:
                answer.append(str(new_nums[idx]+1) + "->" + str(new_nums[idx+1]-1))
                
                
        return answer
                
                
                
                
