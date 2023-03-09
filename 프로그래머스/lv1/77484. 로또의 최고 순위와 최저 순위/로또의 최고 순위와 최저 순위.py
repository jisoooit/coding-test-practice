def solution(lottos, win_nums):
    answer = [0,0]
    num=0
    zero=lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            num+=1
    
    answer[0]=7-(num+zero)
    answer[1]=7-num
    if 7-(num+zero)>6:
        answer[0]=6
    if 7-num>6:
        answer[1]=6
    
    print(answer)
    return answer