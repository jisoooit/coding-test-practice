
        
          
def solution(nums):
    answer = 0
    
    numset = set(nums)
    gift = len(nums)//2
    
    if len(numset) >= gift:
        answer = gift
    else:
        answer = len(numset)
        
    
    
    return answer