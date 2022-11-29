def solution(citations):
    answer = 0
    citations.sort()
    citations_len = len(citations)
    min_c = min(citations)
    max_c = max(citations)

    res = 0
    for i in range(max_c):
        for j in range(citations_len):
            if citations[j]>=i and len(citations[j:]) >= i and len(citations[:j]) <= i:
                answer = max(answer, i)
                break
                
    return answer