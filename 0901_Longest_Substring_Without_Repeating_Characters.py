class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start_point = -1
        answer = 0
        
        for idx, c in enumerate(s):
            
            if c in d:
                start_point = max(start_point, d[c]) #update for start_point(boundary)
            
            d[c] = idx
            
            #update for length
            answer = max(answer, idx-start_point)
            
            
        return answer
