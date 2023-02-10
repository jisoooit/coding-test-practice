s=input()
arr=[0,0]
arr[int(s[0])]+=1
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        arr[int(s[i])]+=1

print(min(arr))