from itertools import product

all=['A','E','I','O','U']
d=[]
N=0

def dfs(depth,md):
    if depth > N:
        return
    else:
        d.append(md)
    for i in range(len(all)):
        if len(md+all[i]) <=N: # 이거 없어도 위에 if에서 걸러지지만 아예 dfs 실행 안되게 하고 싶었음..
            dfs(depth+1, md+all[i])

            
def solution(word):
    answer=0
    global N,d
    N=5
    dfs(0,"")
    d=sorted(d)
    return d.index(word)
# def solution(word):
#     answer=0
    
#     all = []
#     dataset = ['A','E','I','O','U']
#     for i in range(1,6):
#         all += list(product(dataset, repeat=i))

#     for i, a in enumerate(all):
#         all[i]=''.join(a)
    
#     all=sorted(all)

#     return all.index(word)+1
