n=int(input())
arr=[0]*(1000+1)
arr[0]=0
arr[1]=1
arr[2]=2
for i in range(3,1000+1):
    arr[i]=arr[i-1]+arr[i-2]
print(arr[n]%10007)
