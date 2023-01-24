from collections import deque


def solution(queue1, queue2):
    answer = -2
    # 원소 전체 합 구하기    

    queue1=deque(queue1)
    queue2=deque(queue2)

    result=0
    l=len(queue1)
    l2=len(queue2)
    s1=sum(queue1)
    s2=sum(queue2)
    while(True):
        if s1 > s2: 
            n=queue1.popleft()
            queue2.append(n)
            s1-=n
            s2+=n
            result+=1
        elif s1 < s2 :
            n=queue2.popleft()
            queue1.append(n)
            s1+=n
            s2-=n
            result+=1
        else:
            break
        if result == l*3:
            result=-1
            break
    

    return result