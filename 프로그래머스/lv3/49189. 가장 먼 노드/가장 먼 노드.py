from collections import defaultdict
from collections import deque

def bfs(num,graph,visited):
    q=deque([num])
    visited[num]=1
    while q:
        num = q.popleft()
        for i in graph[num]:
            if visited[i]==0:
                visited[i]=visited[num]+1
                q.append(i)




def solution(n, edge):
    answer = 0
    visited=[0]*(n+1)
    graph = defaultdict(list)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    bfs(1,graph,visited)

    answer = visited.count(max(visited))

    return answer

    