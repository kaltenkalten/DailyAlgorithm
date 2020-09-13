class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        
        def backtracking(o, c, cur):
            if o == 0 and c == 0:
                self.result.append(cur)
                return
            if o > 0:
                backtracking(o-1, c, cur+'(')
            if c > 0 and c > o:
                backtracking(o, c-1, cur+')')
                
            
            
        backtracking(n, n, '')
        return self.result
