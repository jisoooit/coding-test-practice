import operator
def solution(N, stages):
    answer=[0 for i in range(N+1)]
    for i in range(1,N+1):
        join=0
        unclear=0
        for stage in stages:
            if stage >=i:
                join+=1
                if stage==i:
                    unclear+=1
            
        if join==0:
            answer[i]=0
        else:
            answer[i]=unclear/join
    
    answer=answer[1:N+1]
    answer_dict=dict(zip(range(1,len(answer)+1),answer))
    answer=sorted(answer_dict.items(), key=operator.itemgetter(1), reverse=True)
    answer=dict(answer)
    answer=list(answer.keys())
    
    
                     


    
    return answer