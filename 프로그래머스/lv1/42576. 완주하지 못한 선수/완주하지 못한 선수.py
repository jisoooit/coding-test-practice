from collections import Counter
def solution(participant, completion):
    answer=''
    
    p_counter = Counter(participant)
    c_counter = Counter(completion)
    
    r_counter = p_counter - c_counter
    
    answer = list(dict(r_counter).keys())[0]

     # return list(answer.keys())[0]
    
    
#     p_dict={x:0 for x in participant}
#     for i in participant:
#         p_dict[i]+=1
#     for i in completion:
#         p_dict[i]-=1
    
#     for key, value in p_dict.items():
#         if value!=0:
#             answer=key

    return answer