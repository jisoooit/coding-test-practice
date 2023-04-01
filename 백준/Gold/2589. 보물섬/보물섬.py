from collections import deque


n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)] 

dy=[0,1,0,-1]
dx=[1,0,-1,0]


def bfs(y,x):
    visited = [[0 for _ in range(m)] for _ in range(n)]

    max_dist=0
    q=deque([[y,x,0]])
    visited[y][x]=1
    while q:
        y, x,dist = q.popleft()
        max_dist = max(max_dist, dist)
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx]=='L' and visited[ny][nx]==0:
                    visited[ny][nx]=1
                    q.append([ny,nx,dist+1])

    return max_dist


ans=0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='L':
            b_dist = bfs(i,j)
            ans = max(ans, b_dist)      

print(ans)
