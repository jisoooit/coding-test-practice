from itertools import permutations

def solution(k, dungeons):
    answer=0
    all=list(permutations(range(len(dungeons)), len(dungeons)))
    case_res=[]
    for case in all:
        nowk=k
        for idx, c in enumerate(case):
            if nowk >= dungeons[c][0]:
                nowk-=dungeons[c][1]
                if idx == len(case)-1:
                      case_res.append(idx+1)
            else:
                case_res.append(idx)
                break

    return max(case_res)