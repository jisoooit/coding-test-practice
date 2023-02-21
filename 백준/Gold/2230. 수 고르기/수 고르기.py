n,m=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(int(input()))

start=0
end=0
ans=2000000000

arr.sort()
while (start<=end and end<n):
    if arr[end]-arr[start]>=m:
        ans=min(ans, arr[end]-arr[start])
        start+=1
    else:
        end+=1
print(ans)
    