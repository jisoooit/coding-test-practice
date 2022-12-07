cnt=0

def dfs(s,depth,numbers, target):
    global cnt
    if depth == len(numbers):
        if s==target:
            cnt+=1
        return
    
    dfs(s+numbers[depth], depth+1,numbers, target)
    dfs(s-numbers[depth], depth+1,numbers, target)

    
def bfs(numbers, target):
    global cnt
    q=deque()
    
    q.append([numbers[0],0])
    q.append([-numbers[0],0])
    while q:
        n,i=q.popleft()
        if i == len(numbers)-1:
            if n == target:
                cnt+=1
        if i<len(numbers)-1:
            q.append([n+numbers[i+1],i+1])
            q.append([n-numbers[i+1],i+1])
            
def solution(numbers, target):
    dfs(0,0,numbers, target)
    #bfs(numbers, target)
    return cnt