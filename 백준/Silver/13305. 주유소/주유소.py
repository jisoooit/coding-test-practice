n=int(input())
load=list(map(int,input().split()))
oil=list(map(int,input().split()))

arr=[]
m=oil[0]
arr.append(0)
for i in range(1,n-1):
  if m>oil[i] and i not in arr:
    m=oil[i]
    arr.append(i)


res=0
for i in range(len(arr)):
  s=sum(load[arr[i]:arr[i+1]]) if i!=len(arr)-1 else sum(load[arr[i]:])
  res+=oil[arr[i]]*s

print(res)