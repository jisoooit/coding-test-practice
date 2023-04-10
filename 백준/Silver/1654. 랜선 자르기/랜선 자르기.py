k,n=map(int,input().split())
line=[]
for _ in range(k):
    line.append(int(input()))

m=min(line)

start=1
end=max(line)
result=0
while (start<=end):
    cnt=0
    mid=(start+end)//2
    for i in line:
        cnt+=i//mid
    if cnt>=n:
        start=mid+1
    else:
        end=mid-1
        
print(end)