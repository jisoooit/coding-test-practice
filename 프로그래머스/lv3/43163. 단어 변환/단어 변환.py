answer=100
visited=[]

def dfs(begin,depth,target,words):
    global answer

    if begin == target:
        if answer > depth:
            answer = depth
        return 
    for i, word in enumerate(words):
        cnt=0
        if visited[i]==0:
            for idx, w in enumerate(word):
                if begin[idx]!=w:
                    cnt+=1
            if cnt<=1:
                visited[i]=1
                dfs(word,depth+1,target,words)
                visited[i]=0
                



def solution(begin, target, words):
    global answer, visited
    visited=[0]*len(words)
    dfs(begin,0,target,words)
    return answer if answer!=100 else 0
    