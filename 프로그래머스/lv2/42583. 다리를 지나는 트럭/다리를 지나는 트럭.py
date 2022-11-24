# 대기트럭 맨 처음거 인덱스로 접근
# 현재 다리위에 있는 트럭들 무게(sum(b)[1]) + 처음거 < 견디는 무게 -> 처음거 반환
# 다리위에 추가 + 추가할때 들어간 시간추가 [[1,[7]][3,[4]][4,[5,1]][6,[6]]]
# 다리 위에서 bl 시간 만큼 지났으면 반환. - 현재시간-들어온시간=bl이면 반환
# 다리위에서 반환할때 다리위에 트럭 없으면 경과시간 리턴
# 다리위 트럭들은 같이 들어온 트럭만 같이 나감 
# 현재시간을 측정해야겠다. 당연함. 모든트럭 지나가는데 걸리는 시간 리턴해야됨
# 다리위에 트럭중 시간 된 트럭있으면 나가고 새 트럭 들어옴

from collections import deque

def bridge_sum(bridge):
    s=0
    for i in bridge:
        s+=sum(i)
        s-=i[0]
    return s


def solution(bridge_length, weight,truck_weights):
    answer = 0
    truck_weights=deque(truck_weights)
    bridge=deque() # 다리위의 트럭들
    truck_num=len(truck_weights)
    finish=[]
    now=0 
    bridge_weight=bridge_sum(bridge) # 다리 위 트럭들의 합
    while len(finish)!=truck_num:
        if len(bridge)!=0:
            bi=0
            while True:
                if len(bridge)>0:
                    if now - bridge[bi][0] == bridge_length:
                        finish.append(bridge.popleft())
                        bi-=1
                    else:
                        break
                    bi+=1
                else:
                    break
        
        if len(truck_weights)>0:
            bridge_weight=bridge_sum(bridge)
            if truck_weights[0]+bridge_weight <= weight:
                bridge.append([now,truck_weights.popleft()])
    
        now+=1
    return now



