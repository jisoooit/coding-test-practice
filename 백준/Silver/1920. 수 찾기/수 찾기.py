n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
arr.sort()

def search(arr, num):
    left=0
    right=n-1
    while(left<=right):
        mid = (left+right)//2
        if arr[mid] == num:
            return True
        elif arr[mid] > num:
            right=mid-1
        else:
            left=mid+1
    
    return False

for i in range(m):
    if search(arr,arr2[i]):
        print(1)
    else:
        print(0)