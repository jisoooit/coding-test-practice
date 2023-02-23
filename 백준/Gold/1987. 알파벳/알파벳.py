

def bfs(y,x):
  global ans
  q=set()
  q.add((x,y,arr[y][x]))
  while q:
    x,y,s=q.pop()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<c and 0<=ny<r and arr[ny][nx] not in s:
        q.add((nx,ny,s+arr[ny][nx]))
        ans=max(ans,len(s)+1)
  
  

dx=[1,0,-1,0]
dy=[0,1,0,-1]
r,c=map(int,input().split())
arr=[list(input()) for i in range(r)]

ans=1
bfs(0,0)
print(ans)