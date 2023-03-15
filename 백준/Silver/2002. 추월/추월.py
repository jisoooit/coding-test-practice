from collections import defaultdict

order=defaultdict(int)
n=int(input())
arr=[]
for i in range(n):
    s=input()
    arr.append(s)
    order[s]=i+1

out=[]
for i in range(n):
    s2=input()
    out.append(s2)
ans=0


for i in range(n-1):
    for j in range(i+1, n):
        if order[out[i]]>order[out[j]]:
            ans+=1
            break
print(ans)