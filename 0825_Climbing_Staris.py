class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1 => 1
        2 => 2
        3 => 2 + 1, 1 + 2
        """
        if n in [1,2]:  return n
        
        preStep = [1, 2]
        
        for i in range(2, n):
            maxStep = preStep[0] + preStep[1]
            preStep = preStep[1], maxStep
            
            
        
        return preStep[-1]
