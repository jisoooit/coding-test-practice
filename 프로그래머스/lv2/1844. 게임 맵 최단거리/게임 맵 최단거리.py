from collections import deque




dy=[0,1,0,-1]
dx=[1,0,-1,0]

def bfs(answer, visited, maps):
    q=deque([[0,0,1]])
    visited[0][0]=1
    while q:
        y,x,cnt = q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny==len(maps)-1 and nx==len(maps[0])-1:
                        return cnt+1
            if 0<=ny<len(maps) and 0<=nx<len(maps[0]):
                if maps[ny][nx]==1 and visited[ny][nx]==0:
                    visited[ny][nx]=1
                    q.append([ny,nx,cnt+1])
                

    return -1


def solution(maps):
    answer = 0
    visited=[[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    return bfs(answer, visited, maps)