class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo = {}
        
        def dfs(rest_s, wordDict, memo):
            if len(rest_s) == 0:
                return True
            
            if rest_s in memo:
                return memo[rest_s]
            
            memo[rest_s] = False
            
            for word in wordDict:
                tmpSize = len(word)
                if len(rest_s) >= tmpSize and rest_s[:tmpSize] == word:
                    memo[rest_s] |= dfs(rest_s[tmpSize:], wordDict, memo)
                    
                    
            return memo[rest_s]
        
        memo[s] = dfs(s, wordDict, memo)
        #print(memo)
        return memo[s]
