n=input()
num=n
cnt=0

while True:
    n=n[-1]+str(sum(list(map(int,n))))[-1]
    cnt+=1
    if num==str(int(n)):
        print(cnt)
        break