def solution(sizes):
    answer = 0
    for size in sizes:
        size.sort()
    maxf, maxs=0,0
    
    for f, s in sizes:
        if maxf<f:
            maxf=f
        if maxs<s:
            maxs=s
    answer=maxf*maxs
        
    return answer