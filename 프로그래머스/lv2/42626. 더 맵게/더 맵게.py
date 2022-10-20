import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) 
    
    while scoville[0] < K: 
        if len(scoville)>1:
            answer += 1
            first = heapq.heappop(scoville) #list의 가장 작은 값을 return하며 삭제
            second = heapq.heappop(scoville) 
            heapq.heappush(scoville, first + second *2)
        else:
            return -1
    return answer