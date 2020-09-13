class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0: return []
        
        intervals.sort()
        
        answer = [intervals[0]]
        
        for first, second in intervals[1:]:
            if answer[-1][1] >= first:
                answer[-1][1] = max(answer[-1][1], second)
                
            else:
                answer.append([first, second])
                
        return answer
