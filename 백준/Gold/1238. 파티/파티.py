from collections import defaultdict
from heapq import heappush, heappop


n,m,x=map(int,input().split())
graph=defaultdict(list)
for _ in range(m):
    i,j,w=map(int,input().split())
    graph[i].append((w,j))

def go_student(start):
    distance=[1000000]*(n+1)

    pq=[] #(최단거리, 현재 노드)
    heappush(pq,(0,start))
    distance[start]=0

    while pq:
        dist, node = heappop(pq)
        
        if dist > distance[node]:
            continue
        
        for weight, next_node in graph[node]:
            time = distance[node]+weight
            if time < distance[next_node]:
                distance[next_node]=time
                heappush(pq, ((time, next_node)))
    
    return distance


go_x=[]
for i in range(1,n+1):
    go_x.append(go_student(i)[x])
come_x=go_student(x)[1:n+1]

answer=0
for i in range(n):
    answer = max(answer, go_x[i]+come_x[i])
print(answer)
