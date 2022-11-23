from collections import deque

def solution(priorities, location):
    cnt=0
    print_list=deque()
    for i,priority in enumerate(priorities):
        print_list.append([priority,i])
    
    while print_list:
        pick = print_list.popleft()
        if len(print_list)==0:
            return cnt+1
        importance = list(zip(*print_list))[0]
        max_important = max(importance)
        if pick[0] < max_important:
            print_list.append(pick)
        else:
            cnt+=1
            if pick[1] == location:
                return cnt