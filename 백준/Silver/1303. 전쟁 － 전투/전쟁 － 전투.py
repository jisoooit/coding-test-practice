import math

n,m = map(int,input().split())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

tw=0
tb=0

visited=[[0 for _ in range(n)] for _ in range(m)]
graph=[]
for i in range(m):
    graph.append(list(input()))

def dfs(y,x, color):
    cnt=1
    visited[y][x]=1
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<m and 0<=nx<n and visited[ny][nx]==0:
            if graph[ny][nx]==color:
                cnt += dfs(ny,nx,color)
    return cnt

for i in range(m):
    for j in range(n):
        if graph[i][j]=='W' and visited[i][j]==0:
            tw+= math.pow(dfs(i,j,'W'),2)
        elif graph[i][j]=='B' and visited[i][j]==0:
            tb+= math.pow(dfs(i,j,'B'),2)


print(int(tw), int(tb))

     