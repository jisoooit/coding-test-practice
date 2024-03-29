from collections import deque




def dfs(num,visited,computers):
    visited[num]=1
    for idx, i in enumerate(computers[num]):
        if i==1 and visited[idx]==0:
            visited[idx]=1
            dfs(idx,visited,computers)

def bfs(num, visited, computers):
    q=deque([num])
    visited[num]=1
    while q:
        num = q.popleft()
        for idx, i in enumerate(computers[num]):
            if i==1 and visited[idx]==0:
                visited[idx]=1
                q.append(idx)

def solution(n, computers):
    answer = 0
    visited=[0]*n
    
    for i in range(n):
        if visited[i]==0:
            # dfs(i,visited, computers)
            bfs(i, visited, computers)
            answer+=1
    
    return answer