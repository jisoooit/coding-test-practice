from heapq import heappush, heappop


sx,sy=map(float,input().split())
ex,ey=map(float, input().split())
n=int(input())
cannon=[]
for _ in range(n):
    x,y=map(float,input().split())
    cannon.append([x,y])

def calc_dist(a, b):
    return ((cannon[a][0]-cannon[b][0])**2 + (cannon[a][1]-cannon[b][1])**2)**0.5

def go_end(idx):
    visited=[0]*(n)
    for i in range(n):
        visited[i]=float('inf')
    
    
    pq=[]
    heappush(pq, (0,idx))
    visited[idx]=0

    while pq:
        time, idx= heappop(pq)

        if time > visited[idx]:
            continue
        for i in range(n):
            if i!=idx:
                cost = visited[idx]
                dist=calc_dist(i,idx)
                if dist-50 > 0:
                    cost += (dist-50)/5 + 2
                else:
                    m = min(dist/5, (50-dist)/5+2)
                    cost+=m
                if cost < visited[i]:
                    visited[i]=cost
                    heappush(pq, (cost, i))
            
    
    for i in range(n):
        end_dist=((ex-cannon[i][0])**2+(ey-cannon[i][1])**2)**0.5
        if end_dist - 50 > 0:
            visited[i]+=(end_dist-50)/5+2
        else:
            visited[i]+=min(end_dist/5, (50-end_dist)/5+2)
        

    return min(visited)


answer=((sx-ex)**2+(sy-ey)**2)**0.5/5
for i in range(n):
    start_case = ((sx-cannon[i][0])**2+(sy-cannon[i][1])**2)**0.5/5
    min_end = go_end(i)
    answer = min(answer, start_case+min_end)

print(answer)
