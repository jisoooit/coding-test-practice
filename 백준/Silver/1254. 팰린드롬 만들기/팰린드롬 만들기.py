
def isPel(s):
    flag=True
    length = len(s)
    for i in range(length//2):
        if s[i]!=s[length-i-1]:
            flag=False
    return flag

ans=0
s=input()
for i in range(len(s)):
    if isPel(s[i:]):
        ans=len(s)+i
        print(ans)
        break
