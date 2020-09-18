def solution(grid, capacity):
  
  
  def dfs(grid, r, c):
    r_adj = [0,0,-1,1]
    c_adj = [1,-1,0,0]
    
    #top, left, bottom, right
    edge = [[0, ]]  


  for r in range(1, len(grid)):
    grid[r][0] += grid[r-1][0]
  for c in range(1, len(grid[0])):
    grid[0][c] += grid[0][c-1]







capacity = 56

grid = [
[4, 3, 3, 2, 5], 
[7, 7, 4, 2, 4],
[1, 5, 4, 6, 5],
[6, 6, 5, 6, 6],
[7, 6, 2, 5, 3]]
