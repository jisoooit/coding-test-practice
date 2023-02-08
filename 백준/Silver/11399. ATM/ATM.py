n=int(input())
arr=list(map(int,input().split()))

arr.sort() # 1 2 3 3 4
ans=0
answer=[]
# 1 / 1+2 / 1+2+3
for i in range(len(arr)):
    ans += arr[i] # 0+1 / 1+2 / 3+3 / 6+3 / 
    answer.append(ans)
print(sum(answer))