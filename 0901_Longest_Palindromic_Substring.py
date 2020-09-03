class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        
        for idx in range(len(s)):
            tmpL, tmpR = self.findPalindrome(idx, idx, s)
            candidate_answer = s[tmpL:tmpR+1]
            answer = max(answer, candidate_answer, key=len)
            
            tmpL, tmpR = self.findPalindrome(idx, idx+1, s)
            candidate_answer = s[tmpL:tmpR+1]
            print(candidate_answer)
            
            answer = max(answer, candidate_answer, key=len)
            
        return answer
    
    def findPalindrome(self, l, r, s):
        if l>=0 and r<len(s) and s[l] != s[r]:
            return l, l
        
        while l>0 and r<len(s)-1 and s[l-1] == s[r+1]:
            l -= 1
            r += 1
            
        return l, r
