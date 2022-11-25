
from collections import deque
def solution(prices):
    answer = []
    dq=deque(prices)
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i] > prices[j]:
                answer.append(j-i)
                break
        else:
            answer.append(len(prices)-1-i)
    
    return answer
        
