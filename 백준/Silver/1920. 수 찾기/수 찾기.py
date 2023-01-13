def binarySearch(arr, a2):
    start =0
    end = len(arr)-1
    while start <=end:
        mid=(start+end)//2
        if arr[mid] == a2:
            return 1
        elif arr[mid] > a2:
            end=mid-1
        else:
            start=mid+1
    return 0

n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
arr.sort()
for a2 in arr2:
    print(binarySearch(arr,a2))
