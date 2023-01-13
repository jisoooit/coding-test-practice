 
n,k =map(int,input().split())
arr=[ int(input()) for _ in range(n)]
arr.sort(reverse=True)
cnt=0
for i in range(len(arr)):
    if k >= arr[i]:
        cnt += k//arr[i]
        k=k%arr[i]
        if k<=0:
            break

print(cnt)