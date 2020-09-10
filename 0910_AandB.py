import copy

def solution(a):
    
    b = [0 * len(a[0])] * len(a)
    
    cnt_row = [True] * len(a) 
    cnt_col = [0] * len(a[0])
    
    for r in range(len(a)):
        for c in range(len(a[0])):
            cnt_col[c] += a[r][c]
            
    global cnt
    cnt = 0
    
    def backtracking(a, b, r, c, cnt_row, cnt_col, level):
        global cnt
        #print(r, c, cnt_row, cnt_col)
        if r == len(a)-1 and c == len(a[0]) and cnt_row[r] == True and sum(cnt_col) == 0:
            cnt += 1
            return
        
        if r >= len(a):
            return
        
        if c >= len(a[0]):
            if cnt_row[r] == True:
                c = 0
                r += 1
            else:
                return
        
        if cnt_col[c] > len(a) - r:
            return
        
        tmp_row = copy.deepcopy(cnt_row) #cnt_row[:]
        tmp_col = copy.deepcopy(cnt_col) #cnt_col[:]
        #print(r, c, cnt_col[c], 'Z', level)
        backtracking(a, b, r, c+1, tmp_row, tmp_col, level+1) # 0
        #print(r, c, tmp_col[c], 'Y', level)
        if cnt_col[c] > 0: # 1
            #print(r, c, "T")
            cnt_col[c] -= 1
            cnt_row[r] = not cnt_row[r]
            backtracking(a, b, r, c+1, cnt_row, cnt_col, level+1)
        #cnt_row = tmp_row
        #cnt_col = tmp_col
        
    backtracking(a, b, 0, 0, cnt_row, cnt_col, 0)
    return cnt
    
     
a1 = [[0,1,0],[1,1,1],[1,1,0],[0,1,1]]
#a1 = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
a2 = [[1,0,0],[1,0,0]]
a3 = [[1,0,0,1,1], [0,0,0,0,0], [1,1,0,0,0], [0,0,0,0,1]] 
print(solution(a1))
print(solution(a2))
print(solution(a3))
