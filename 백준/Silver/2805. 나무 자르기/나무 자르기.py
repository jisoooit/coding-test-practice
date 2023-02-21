n,m=map(int,input().split())
a=list(map(int,input().split()))
start=1
end=max(a)

result=0
while(start<=end):
  sum=0
  mid=(start+end)//2
  for i in a:
    if i>mid:
      sum+=i-mid
  if sum<m:
    end=mid-1
  else:
    result=mid
    start=mid+1

print(result)