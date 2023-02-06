n,k=map(int,input().split())
arr=[]
for i in range(1,int(n**(0.5))+1):
    if n%i==0:
        arr.append(i)
        arr.append(n//i)
arr=list(set(arr))
arr.sort()

if len(arr)<k:
    print(0)
else:
    print(arr[k-1])