n,m=map(int,input().split())
arr=list(map(int,input().split()))


s=0
count=0
start=0
end=0

while True:
    if s>m:
        s-=arr[start]
        start+=1
    elif end==n:
        break
    else:
        s+=arr[end]
        end+=1
    if s==m:
        count+=1

print(count)