cnt=0

while True:
    s = list(input())
    ans=0
    if '-' in s:
        break

    
    stack=[]

    for i in s:
        if i=='{':
            stack.append(i)
        else:
            if stack: # 스택이 안비었다면
                stack.pop()
            else:
                ans+=1
                stack.append('{')

   
    ans+=len(stack)//2

    cnt+=1
    print(str(cnt)+".",ans)
