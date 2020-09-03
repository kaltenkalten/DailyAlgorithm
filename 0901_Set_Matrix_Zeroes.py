class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        c_tmp = [1] * len(matrix[0])
        r_tmp = [1] * len(matrix)
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                c_tmp[c] = int(bool(c_tmp[c] * matrix[r][c]))
                r_tmp[r] = int(bool(r_tmp[r] * matrix[r][c]))
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = matrix[r][c] * c_tmp[c] * r_tmp[r]
                
                
