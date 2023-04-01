n,m,h = map(int,input().split())
graph = [[0]*(n+1) for _ in range(h+1)]
combi=[]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1

def check():
    for i in range(1,n+1):
        now=i
        for j in range(1,h+1):
            if graph[j][now-1]:
                now-=1
            elif graph[j][now]:
                now+=1
        if now!=i:
            return False
    return True

def dfs(depth, idx):
    global ans

    if depth>=ans:
        return
    if check(): 
        ans=depth
        return

    for c in range(idx, len(combi)):
        x,y=combi[c]
        if not graph[x][y-1] and not graph[x][y+1]:
            graph[x][y]=1
            dfs(depth+1, c+1)
            graph[x][y]=0


for i in range(1,h+1):
    for j in range(1,n):
        if not graph[i][j-1] and not graph[i][j+1] and not graph[i][j]:
            combi.append([i,j])


ans=4
dfs(0,0)
print(ans if ans<4 else -1)