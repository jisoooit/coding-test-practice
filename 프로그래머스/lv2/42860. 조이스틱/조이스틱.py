def solution(name):
       
    answer=0
    min_dist = len(name)-1
    for idx,n in enumerate(name):
        answer += min(ord(n)-ord('A'), ord('Z')-ord(n)+1)
        next=idx+1
        while next<len(name) and name[next]=='A':
            next+=1
        min_dist = min([min_dist, 2*idx+len(name)-next, 2*(len(name)-next)+idx])

    return answer + min_dist
    