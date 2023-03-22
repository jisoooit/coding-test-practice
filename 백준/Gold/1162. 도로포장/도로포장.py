from heapq import heappush, heappop
from collections import defaultdict


n,m,k=map(int,input().split())
graph=defaultdict(list)
for _ in range(m):
    s,e,w=map(int,input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))



d=[[float('inf')]*(k+1) for _ in range(n+1)]

def dijkstra(start):
    
    
    pq=[]
    heappush(pq, (0,start,0))
    for i in range(k+1):
        d[start][i]=0

    while pq:
        now_dist, node, p = heappop(pq)
        if d[node][p]<now_dist:
            continue

        if p+1<=k:
            for (next_dist, next) in graph[node]:
                if d[next][p+1]>now_dist:
                    d[next][p+1]=now_dist
                    heappush(pq,(now_dist, next, p+1))
        
        for (next_dist, next) in graph[node]:
            if d[next][p] > now_dist + next_dist:
                d[next][p]=now_dist+next_dist
                heappush(pq, (now_dist+next_dist, next, p))

dijkstra(1)

ans=float('inf')
for i in range(k+1):
    ans=min(ans,d[n][i])
print(ans)
            