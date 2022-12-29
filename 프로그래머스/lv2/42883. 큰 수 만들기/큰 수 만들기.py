def solution(number, k):
    result=""
    ans=[]
    
    for num in number:
        if k>0:
            while ans and ans[-1] < num:
                ans.pop()
                k-=1
                if k==0:
                    break
        ans.append(num)
  
    result=''.join(ans)
    return result[:len(number)-k]