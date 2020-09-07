class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(grid, r, c):
            move_c = [0,0,1,-1]
            move_r = [1,-1,0,0]
            
            for i in range(4):
                adj_r = move_r[i] + r
                adj_c = move_c[i] + c
                if 0<=adj_r<len(grid) and 0<=adj_c<len(grid[0]) and grid[adj_r][adj_c] == '1':
                    grid[adj_r][adj_c] = '0'
                    dfs(grid, adj_r, adj_c)
            
            
            
        
        count = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    grid[r][c] == '0'
                    dfs(grid, r, c)
                    
                    
        return count
