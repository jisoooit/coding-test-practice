def solution(n, lost, reserve):

    answer=0
    lost.sort()
    reserve.sort()
    lost_copy=lost[:]
    for l in lost_copy:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    
    answer=n-len(lost)
    for l in lost: #작은거부터 올라가니까
        if l-1 in reserve: #작은거 있으면 부터 검사하는거임
            answer+=1
            reserve.remove(l-1)
        elif l+1 in reserve:
            answer+=1
            reserve.remove(l+1)

    
    return answer