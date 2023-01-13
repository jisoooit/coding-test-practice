answer = 0

t=int(input())
for _ in range(t):
    answer=0
    n,m = map(int,input().split())

    for a in range(1,n):
        for b in range(a+1,n):
            if ((a*a + b*b+ m) % (a*b)) ==0:
                answer+=1  
    print(answer)