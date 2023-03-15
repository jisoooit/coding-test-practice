n=list(map(int,input()))
original = int(''.join(str(s) for s in n))
visit=[0]*len(n)
new = []
ans=1000000

def dfs(depth):
    global ans

    if depth==len(n):
        new_num=int(''.join(str(s) for s in new))
        if new_num>original:
            ans=min(ans,new_num)
        return
    for i in range(len(n)):
        if visit[i]==0:
            visit[i]=1
            new.append(n[i])
            dfs(depth+1)
            visit[i]=0
            new.pop()

dfs(0)
print(ans) if ans!=1000000 else print(0)

