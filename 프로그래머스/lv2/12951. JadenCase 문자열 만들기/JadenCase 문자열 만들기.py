def solution(s):
    answer = ''
    arr = list(s)
    for i in range(1,len(arr)):
        if arr[i-1]==' ':
            arr[i]=arr[i].upper()
        else:
            arr[i]=arr[i].lower()
        
    if arr[0]!=' ':
        arr[0]=arr[0].upper()
    answer = ''.join(arr)
    return answer