
def adj_cell(cells, r, c):
    neighbor_dead = 0
    neighbor_live = 0

    adj = [[0,-1], [-1,0], [1,0], [0,1], [-1,-1], [-1,1], [1,1], [1,-1]]

    for r_, c_ in adj:
        if 0 <= r+r_ < len(cells) and 0 <= c+c_ < len(cells[0]):
            if cells[r+r_][c+c_] in [0,2]:
                neighbor_dead += 1
            else:
                neighbor_live += 1

    return neighbor_live, neighbor_dead

def solution(cells):
    # dead : 0, 2, live : 1, 3
    # dead -> live : 2
    # live -> dead : 3
    for r in range(len(cells)):
        for c in range(len(cells[0])):
            neighbor_live, neighbor_dead = adj_cell(cells, r, c)
            print(neighbor_live, neighbor_dead)
            if cells[r][c] in [1,3]:
                if neighbor_live < 2 or neighbor_live > 3:
                    cells[r][c] = 3
                #if neighbor_live in [2,3]:
                #    pass
            else:
                if neighbor_live == 3:
                    cells[r][c] = 2
    d = {0:0, 1:1, 2:1, 3:0}
    print(cells) 
    for r in range(len(cells)):
        for c in range(len(cells[0])):
            cells[r][c] = d[cells[r][c]]

    return cells

cells = [[0,1,0],
[0,0,1],
[1,1,1],
[0,0,0]]

print(solution(cells))
