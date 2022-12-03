from collections import deque
import copy

answer=100
visited=[]
new_wires=[]

def bfs(num, bfswires):
    global visited
    cnt=0
    visited[num]=1
    q=deque([num])
    while q:
        nxt= q.popleft()
        visited[nxt]=1
        cnt+=1
        for i in bfswires[nxt]:
            if visited[i]==0:
                q.append(i)
                visited[i]=1

    return cnt

def solution(n, wires):
    global N, visited, new_wires, answer
    max_v = max(map(max,wires))
    new_wires=[[] for _ in range(max_v+1)]
    
    for wire in wires:
        new_wires[wire[0]].append(wire[1])
        new_wires[wire[1]].append(wire[0])

    for wire in wires:
        visited = [0] * (max_v+1)
        bfswires = copy.deepcopy(new_wires)
        bfswires[wire[0]].remove(wire[1])
        bfswires[wire[1]].remove(wire[0])
        
        answer = min(answer, abs(bfs(wire[0],bfswires)-bfs(wire[1],bfswires)))
        
    return answer
