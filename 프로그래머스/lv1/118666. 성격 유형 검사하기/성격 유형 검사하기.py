def solution(survey, choices):
    answer = ''
    alpha=["R","T","C","F","J","M","A","N"]
    score=dict(zip(alpha,[0]*8))
    for i in range(len(choices)):
        if choices[i]>4:
            score[survey[i][1]]+=(choices[i]-4)
        elif choices[i]<4:
            score[survey[i][0]]+=(4-choices[i])
    
    for i in range(0,8,2):
        if score[alpha[i]]>=score[alpha[i+1]]:
            answer+=alpha[i]
        elif score[alpha[i]]<score[alpha[i+1]]:
            answer+=alpha[i+1]
            
    print(score)
    
    return answer