from collections import defaultdict
from collections import deque
n,m,v=map(int,input().split())
graph = defaultdict(list)
visited=[0]*(n+1)

def dfs(num):
    visited[num]=1
    print(num, end=' ')
    for i in graph[num]:
        if visited[i]==0:
            dfs(i)

def bfs(num):
    q=deque([num])
    visited[num]=1
    while q:
        num = q.popleft()
        print(num,end=' ')
        for i in graph[num]:
            if visited[i]==0:
                visited[i]=1
                q.append(i)


for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

dfs(v)
print()
visited=[0]*(n+1)
bfs(v)
