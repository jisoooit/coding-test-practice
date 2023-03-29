import copy


n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)] 

cnt=0
cctv=[]
for i in range(n):
    for j in range(m):
        if 0<graph[i][j]<6:
            cctv.append([graph[i][j],i,j])

cnt = len(cctv)

# 오 아래 왼 위
dy=[0,1,0,-1]
dx=[1,0,-1,0]

mode = [
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,3],[0,1],[1,2],[2,3]],
    [[0,2,3],[0,1,2],[1,2,3],[3,0,1]],
    [[0,1,2,3]]
]

def calc(temp, y,x,mm):
    for i in mm:
        ny=y
        nx=x 
        while True:
            ny+=dy[i]
            nx+=dx[i]
            if 0>ny or ny>=n or 0>nx or nx>=m:
                break
            if temp[ny][nx]==6:
                break
            elif temp[ny][nx]==0:
                temp[ny][nx]=7



def dfs(depth, arr):
    global min_value

    if depth==cnt:
        ans=0
        for i in range(n):
            ans+=arr[i].count(0)
        min_value = min( min_value, ans )
        return
    temp = copy.deepcopy(arr)
    cctv_num, y, x = cctv[depth]
    for i in mode[cctv_num]:
        calc(temp, y, x, i)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)

min_value=int(1e9)
dfs(0, graph)
print(min_value)