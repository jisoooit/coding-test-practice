n,k=map(int,input().split())
d=[[0]*(k+1) for _ in range(n+1)]
product=[[0,0]]

for _ in range(n):
    w,v=map(int,input().split())
    product.append([w,v])


for i in range(1,n+1):
    for j in range(1,k+1):
        w=product[i][0]
        v=product[i][1]

        if j<w:
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(v+d[i-1][j-w], d[i-1][j])

print(d[n][k])