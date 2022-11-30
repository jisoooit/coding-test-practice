def solution(brown, yellow):
    answer=[]
    cand=[]
    for i in range(1,int(yellow**0.5)+1):
        if yellow % i ==0:
            cand.append([yellow//i, i])
    
    for c in cand:
        if c[0]*2 + c[1]*2 + 4 ==brown:
            return [c[0]+2,c[1]+2]; 