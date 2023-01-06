from collections import defaultdict


def solution(N, number):
    dp = defaultdict(set)
    
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i+1):
            for x in dp[j]:
                for y in  dp[i-j]:
                    dp[i].add(x+y)
                    dp[i].add(x-y)
                    dp[i].add(x*y)
                    if y!=0:
                        dp[i].add(x//y)


    for i in range(1,9):
        if number in dp[i]:
            return i

    return -1
