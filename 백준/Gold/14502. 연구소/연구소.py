from collections import deque
import copy

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
virus_visit=[[0 for _ in range(m)] for _ in range(n)]
visit=[[0 for _ in range(m)] for _ in range(n)]
dy=[0,1,0,-1]
dx=[1,0,-1,0]
ans=0

def dfs(depth):
    global ans

    if (depth == 3):
        virus()
        return
    for i in range(n):
        for j in range(m):
            if board[i][j]==0 and visit[i][j]==0:
                visit[i][j]=1
                board[i][j]=1
                dfs(depth+1)
                visit[i][j]=0
                board[i][j]=0
                

def virus():
    q=deque()
    board_copy=copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if board_copy[i][j]==2:
                q.append([i,j])

    while q:
        y,x=q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<m and board_copy[ny][nx]==0 :
                q.append([ny,nx])
                board_copy[ny][nx]=2
    
      
    global ans
    cnt=0

    for i in range(n):
        cnt+=board_copy[i].count(0)
    ans=max(ans,cnt)



dfs(0)
print(ans)