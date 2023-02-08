n=int(input())
arr=list(map(int,input().split()))

arr.sort() # 1 2 3 3 4
ans=0
part=0
answer=[]
for i in range(len(arr)):
    part += arr[i] # 0+1 / 1+2 / 3+3 / 6+3 / 
    ans+=part
print(ans)