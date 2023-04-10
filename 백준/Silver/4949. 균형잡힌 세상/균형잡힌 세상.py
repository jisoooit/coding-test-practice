while True :
    s=input()

    if s=='.':
        break

    stack = []
    flag=0

    for i in s:
        if i=='[' or i=='(':
            stack.append(i)
        elif i==']' or i==')':
            if stack:
                gal=stack.pop()
                if i==']' and gal=='(':
                    flag=1
                elif i==')' and gal=='[':
                    flag=1
            else:
                flag=1
    
    
    if flag==1:
        print("no")
    elif len(stack)==0:
        print("yes")
    else:
        print("no")

