from collections import deque

visited=[[0 for _ in range(102)] for _ in range(102)]
dy=[0,1,0,-1]
dx=[1,0,-1,0]

def bfs(y,x,rectangle,itemX,itemY):
    q=deque([[y,x,0]])
    visited[y][x]=1
    while q:
        y,x,dist = q.popleft()
        
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny==itemY and nx==itemX:
                    return dist+1
            
            if not (1<=nx<=100 and 1<=ny<=100) or visited[ny][nx]==1:
                continue


            flag=False
            for idx,rect in enumerate(rectangle):
                if (nx==rect[0] or nx==rect[2]) and rect[1]<=ny<=rect[3] and (x+dx[i]/2 ==rect[0] or x+dx[i]/2 ==rect[2]) and rect[1]<=y+dy[i]/2<=rect[3]:
                    flag=True  
                if (ny==rect[1] or ny==rect[3]) and rect[0]<=nx<=rect[2] and (y+dy[i]/2 ==rect[1] or y+dy[i]/2 ==rect[3]) and  rect[0]<=x+dx[i]/2<=rect[2]:
                    flag=True
                    
                if rect[0]<x+dx[i]/2<rect[2] and rect[1]<y+dy[i]/2<rect[3]:
                    flag=False
                    break
                if rect[0]<nx<rect[2] and rect[1]<ny<rect[3]:
                    flag=False
                    break
            
            if flag and visited[ny][nx]==0:
                visited[ny][nx]=1
                q.append([ny,nx,dist+1])

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    for rec in rectangle:
        rec[0] *=2
        rec[1] *=2
        rec[2] *=2
        rec[3] *=2
    characterX *=2
    characterY *=2
    itemX *= 2
    itemY *= 2
    visited = [[0]*101 for _ in range(101)]
    answer=bfs(characterY,characterX,rectangle,itemX,itemY)

    return answer//2