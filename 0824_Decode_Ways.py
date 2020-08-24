ass Solution:
    def numDecodings(self, s: str) -> int:
        
        # Dynamic Programming
        
        memo = {}
        
        
        def dfs(rest_s, memo):
            if len(rest_s) == 0:
                return 1
        
            if rest_s[0] == '0':
                return 0
        
            if rest_s in memo:
                return memo[rest_s]
            
            memo[rest_s] = dfs(rest_s[1:], memo)
                
            if len(rest_s) > 1 and 10 <= int(rest_s[:2]) <= 26:
                #print(rest_s[:2])
                memo[rest_s] += dfs(rest_s[2:], memo)
                
            
            return memo[rest_s]
        
        memo[s] = dfs(s, memo)
        #print(memo)
        return memo[s]
