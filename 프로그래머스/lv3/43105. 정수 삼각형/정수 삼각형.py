# 0 - 0
# 1 - 0 1
# 2 - 1 2
# n - n-1


def solution(triangle):
    answer = 0
    dev_tri=[]
    for i in range(len(triangle)):
        dev_tri.append([0 for _ in range(i+1)])
   
    dev_tri[0][0]=triangle[0][0]
    for i, trian in enumerate(triangle):
        if i>0:
            for j in range(len(trian)):
                dev_tri[i][j]=triangle[i][j]
                if j==0:
                    dev_tri[i][j]+=dev_tri[i-1][j]
                elif j==len(trian)-1:
                    dev_tri[i][j]+=dev_tri[i-1][j-1]
                else:
                    dev_tri[i][j]+=max(dev_tri[i-1][j-1],dev_tri[i-1][j])
    
    answer=max(dev_tri[len(triangle)-1])
    return answer