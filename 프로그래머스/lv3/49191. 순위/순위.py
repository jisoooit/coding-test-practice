# 모든 숫자와 관계가 있어야 함.
# 나를 이긴 사람이 2명, 나한테 진사람이 2명이면 나는 3등
# 나를 이긴 사람이 1명, 나한테 진사람이 3명이면 나는 2등
# 내가 2등인데 이긴사람 1명 있으면 그사람은 1등
# 내가 4등인데 진 사람 1명있으면 그 사람은 5등

# 4: 3,2
# 3: 2
# 1: 2
# 2: 5


# 4 : 3, 2, 5
# 3 : 2, 5
# 1 : 2 ,5
# 2 : 5
# 5 : 

[[4,3],[4,2],[3,2],[2,1],[2,5]]

# 4: 3, 2
# 3: 2
# 2: 1, 5

# 4: 3, 2, 1, 5
# 3: 2, 1, 5
# 2: 1, 5
# 1:
# 5:
from collections import defaultdict
from collections import deque

def bfs(num, graph,visited):
    q=deque([num])
    visited[num]=1   
    while q:
        num=q.popleft()
        for i in graph[num]:
            if visited[i]==0:
                q.append(i)
                graph[num].extend(graph[i])
                visited[i]=1

def solution(n, results):
    answer = 0
    graph = defaultdict(list)
    grade=[0]*(n+1)

    for i in range(1,n+1):
        graph[i]=[]
    for a, b in results:
        graph[a].append(b)
    
#     for key, values in graph.items():
#         for v in values:
#             graph[key].extend(graph[v])
#         graph[key]=list(set(graph[key]))
    

    for i in range(1,n+1):
        visited=[0]*(n+1)
        bfs(i,graph,visited)
        graph[i]=list(set(graph[i]))
    
    for i in range(1,n+1):
        if len(graph[i]) == n-1:
            grade[1]=i
        else:
            win=len(graph[i])
            lose=0
            for v in graph.values():
                if i in v:
                    lose+=1
            
            if win+lose == n-1:
                grade[lose+1]=i
    
    
    for g in grade:
        if g!=0:
            answer+=1

    return answer

    