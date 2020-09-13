class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #if len(digits)  == 0:   return []
        self.result = []
        d = {1:[''], 2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'],9:['w','x','y','z']}
        
        def backtracking(rest_digits, cur_str):
            if len(rest_digits) == 0:
                if cur_str != "":
                    self.result.append(cur_str)
                return
            
            for ch in d[int(rest_digits[0])]:
                backtracking(rest_digits[1:], cur_str + ch)
            

        backtracking(digits, '')
        return self.result
