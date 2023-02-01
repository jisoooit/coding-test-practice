def solution(id_list, report, k):
    answer = []
    report=set(report)
    report=list(report)
    arr=[[] for i in range(len(report))]
    num=[0 for _ in range(len(id_list))]
    di=dict(zip(id_list, num))
    
    for i in range(len(report)):
        arr[i]=report[i].split()
        di[arr[i][1]]+=1
    
    for i in range(len(report)):
        if di[arr[i][1]]>=k:
            num[id_list.index(arr[i][0])]+=1
            
    
    return num