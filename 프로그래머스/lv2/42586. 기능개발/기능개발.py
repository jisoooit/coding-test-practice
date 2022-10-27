from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    # 7일은 되야.. 3일, 9일 
    # 5일, 10일, 1일, 1일, 20일, 1일 
    # 내 앞의 작업이 끝나고, 그 일자 안에 내 작업이 끝나면 내앞의 작업과 나는 같이 배포된다.
    # 내앞의 작업이 끝나고, 그 일자 안에 내 작업이 끝나지 않았다면 내 앞의 작업과 나는 따로 
    # 10 1 4 - 예외 
    
    q=[]
    
    time = []
    
    for i in range(len(progresses)):
        time.append(math.ceil((100-progresses[i])/speeds[i] ))
        
    cnt=1
    q.append(time[0])
    for i in range(1, len(time)):
        if q[-1] >= time[i]:
            cnt+=1
        else:
            q.append(time[i])
            answer.append(cnt)
            cnt=1
    answer.append(cnt)
    
    
    return answer