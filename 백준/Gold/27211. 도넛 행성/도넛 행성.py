from collections import deque
n,m=map(int,input().split())
visited=[[0 for _ in range(m)] for _ in range(n)]

dy=[0,1,0,-1]
dx=[1,0,-1,0]

def bfs(y,x):
    q=deque([[y,x]])
    visited[y][x]=1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if ny==-1:
                ny=n-1
            if nx==-1:
                nx=m-1
            if ny==n:
                ny=0
            if nx==m:
                nx=0
            if graph[ny][nx]==0 and visited[ny][nx]==0:
                visited[ny][nx]=1
                q.append([ny,nx])


graph=[list(map(int,input().split())) for _ in range(n)]

cnt=0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0 and visited[i][j]==0:
         
            cnt+=1
            bfs(i,j)

print(cnt)
