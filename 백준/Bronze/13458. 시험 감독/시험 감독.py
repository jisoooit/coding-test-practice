import math

n=int(input())
arr=list(map(int,input().split()))
b,c=map(int,input().split())

for i in range(len(arr)):
    arr[i]-=b
cnt=n
for i in range(len(arr)):
    if arr[i] > 0:
      cnt+=math.ceil(arr[i]/c)
print(cnt)