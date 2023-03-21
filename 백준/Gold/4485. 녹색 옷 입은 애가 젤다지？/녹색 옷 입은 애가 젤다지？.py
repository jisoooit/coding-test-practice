from heapq import heappush, heappop


dy=[0,1,0,-1]
dx=[1,0,-1,0]
idx=0

def escape(y,x):
    visited=[[float('inf')]*n for _ in range(n)]

    pq=[]
    heappush(pq, (graph[y][x],y,x))
    visited[y][x]=graph[y][x]

    while pq:
        cost , y,x= heappop(pq)

        if cost > visited[y][x]:
            continue
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<n :
                c = graph[ny][nx]+ visited[y][x]
                if c < visited[ny][nx]:
                    visited[ny][nx]=c
                    heappush(pq, (c,ny,nx))
    
    return visited[n-1][n-1]


while True:
    n=int(input())
    if n==0:
        break

    idx+=1
    graph=[list(map(int,input().split())) for _ in range(n)]
    print("Problem",str(idx)+":",escape(0,0))
 
