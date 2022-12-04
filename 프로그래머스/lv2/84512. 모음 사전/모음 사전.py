from itertools import product

def solution(word):
    answer=0
    
    all = []
    dataset = ['A','E','I','O','U']
    for i in range(1,6):
        all += list(product(dataset, repeat=i))

    for i, a in enumerate(all):
        all[i]=''.join(a)
    
    all=sorted(all)

    return all.index(word)+1
