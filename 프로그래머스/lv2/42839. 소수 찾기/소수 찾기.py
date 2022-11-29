from itertools import permutations

def filter(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer=0
    numbers = list(numbers)
    print(numbers)
    cand = set()
    for i in range(1,len(numbers)+1):
        for number in list(permutations(numbers,i)):
            n=str(int(''.join(number)))

            cand.add(n)
    print(cand)
    for i in cand:
        if filter(int(i)):
            answer+=1
    return answer
   
