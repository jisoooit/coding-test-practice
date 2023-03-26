from collections import deque

def solution(s):
    
    # 스택이 비면 true, 스택에 남아있으면 false
    dq=deque()
    for index, i in enumerate (s):
        if i=='(':
            dq.append(i)
        elif i==')':
            if len(dq)==0:
                return False
            dq.pop()
    
    return True if len(dq) == 0 else False
        
