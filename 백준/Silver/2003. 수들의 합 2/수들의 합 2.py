n,m=map(int,input().split())
arr=list(map(int,input().split()))

ans=0

for i in range(n):
    s=0
    for j in range(i, n):
        s+=arr[j]
        if s==m:
            ans+=1
            break

print(ans)
