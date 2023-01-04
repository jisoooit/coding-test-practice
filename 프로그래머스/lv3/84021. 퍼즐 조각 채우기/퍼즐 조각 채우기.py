import copy

dy=[0,1,0,-1]
dx=[1,0,-1,0]

def dfs(graph, y, x, position, n, num):
    ret = [position]
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<n and 0<=nx<n and graph[ny][nx]==num:
            graph[ny][nx]=2
            ret+=dfs(graph, ny, nx, [position[0]+dy[i], position[1]+dx[i]], n, num)
    
    return ret

        
def rotate(lst):
    n = len(lst)
    
    ret = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = lst[i][j]
    
    return ret

def solution(game_board, table):
    answer = 0
    game_board_copy = copy.deepcopy(game_board)
    
    n = len(game_board)
    block = []
    
    for i in range(n):
        for j in range(n):
            if game_board_copy[i][j] == 0:
                game_board_copy[i][j] = 2
                result = dfs(game_board_copy, i, j, [0, 0], n, 0)[1:]
                block.append(result)
    for r in range(4):
        table = rotate(table)
        table_rotate_copy = copy.deepcopy(table)

        for i in range(n):
            for j in range(n):
                if table_rotate_copy[i][j] == 1:
                    table_rotate_copy[i][j] = 2
                    result = dfs(table_rotate_copy, i, j, [0, 0], n, 1)[1:]
                    if result in block:
                        block.pop(block.index(result))
                        answer += (len(result) + 1)
                        table = copy.deepcopy(table_rotate_copy)
                        
                    else:
                        table_rotate_copy = copy.deepcopy(table)
    return answer