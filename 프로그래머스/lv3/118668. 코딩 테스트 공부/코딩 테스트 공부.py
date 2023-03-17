def solution(alp, cop, problems):
    answer = 0
    max_alp=0
    max_cop=0

    for a,b,c,d,e in problems:
        max_alp= max(max_alp, a)
        max_cop = max(max_cop, b)


    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')
    dp = [[INF]*(max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop]=0 # dp[i][j]의 의미 : 알고력 i, 코딩력 j를 도달할 수 있는 최단시간
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i+1<=max_alp:
                dp[i+1][j]=min(dp[i+1][j], dp[i][j]+1)
            if j+1<=max_cop:
                dp[i][j+1]=min(dp[i][j+1],dp[i][j]+1)

            for a,b,c,d,e in problems:
                if i>= a and j>=b:
                    new_alp = min(i+c, max_alp) #max값과 비교하여 min값으로 정하는 이유는 max이상이면 그냥 max에 저장하면 되기 때문
                    new_cop = min(j+d, max_cop)
                    dp[new_alp][new_cop]=min(dp[new_alp][new_cop], dp[i][j]+e)

    return dp[-1][-1]