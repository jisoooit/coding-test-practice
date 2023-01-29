from itertools import combinations

def isprime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
    
def solution(nums):
    answer = 0
    
    for l in combinations(nums, 3):
        three_sum=sum(l)
        if isprime(three_sum):
            answer+=1
    return answer