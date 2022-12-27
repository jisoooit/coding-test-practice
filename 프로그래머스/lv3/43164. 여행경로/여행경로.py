from collections import deque


def bfs(start_idx,tickets):
    answer=["ICN"]
    arr=[]
    visited=[0]*len(tickets)
    q=deque()
    q2=deque()
    for idx,ticket in enumerate(tickets):
        if ticket[0]=="ICN":
            visited[idx]=1
            q.append(ticket[1])
            q2.append([answer+[ticket[1]],visited[:]])
            visited[idx]=0


    while q:
        end=q.popleft()
        cur_arr,visited=q2.popleft()
        if len(cur_arr)==len(tickets)+1:
            return cur_arr
        for idx, ticket in enumerate(tickets):

            if ticket[0]==end and visited[idx]==0:
    
                visited[idx]=1
                q.append(ticket[1])
                q2.append([cur_arr+[ticket[1]],visited[:]])
                visited[idx]=0
            
            
def dfs():
    t_dict = defaultdict(list)
    for start, end in tickets:
        t_dict[start].append(end)
    for k in t_dict:
        t_dict[k].sort()

    print(t_dict)
    s=["ICN"]
    p=[]

    while s:
        n=s[-1]
        if t_dict[n]!=[]:
            s.append(t_dict[n].pop(0))
        else:
            p.append(s.pop())
    
    return p[::-1]

def solution(tickets):
    tickets.sort(key=lambda x:(x[0],x[1]))
    
    for idx,ticket in enumerate(tickets):
        if ticket[0]=="ICN":
            return bfs(idx,tickets)