n=int(input())
arr=[0]*( 1000000+1)
arr[1]=1 #1
arr[2]=2 #11 00
arr[3]=3 #001 100 111 
arr[4]=5 #0011 1001 1100 1111 0000
# 00111 10011 11001 11111 00001 / 00100 10000 11100

for i in range(3,1000000+1):
    arr[i]=(arr[i-1]+arr[i-2])%15746
print(arr[n]%15746)