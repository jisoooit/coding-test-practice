from itertools import permutations

answer=0
def dfs(cnt,k,dungeons):
    global answer
    if cnt > answer:
        answer=cnt
    for i in range(len(dungeons)):
        if visited[i]==0 and dungeons[i][0]<=k:
            visited[i]=1
            dfs(cnt+1, k-dungeons[i][1],dungeons)
            visited[i]=0

            
def solution(k,dungeons):
    global visited
    
    visited=[0]*len(dungeons)
    
    dfs(0,k,dungeons)
    return answer

# def solution(k, dungeons):
#     answer=0
#     all=list(permutations(range(len(dungeons)), len(dungeons)))
#     case_res=[]
#     for case in all:
#         nowk=k
#         for idx, c in enumerate(case):
#             if nowk >= dungeons[c][0]:
#                 nowk-=dungeons[c][1]
#                 if idx == len(case)-1:
#                       case_res.append(idx+1)
#             else:
#                 case_res.append(idx)
#                 break

#     return max(case_res)