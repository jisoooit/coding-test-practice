# 왼쪽, 위의 경우의수를 더하면 되는듯? 
# 최단경로인지 어케암..? 

def solution(m, n, puddles):
    answer = 0
    dp=[[0 for _ in range(m)]for _ in range(n)]
    dp[0][0]=1
    for i in range(len(puddles)): #[x,y]
        dp[puddles[i][1]-1][puddles[i][0]-1]=0
        
    
    for i in range(0,n):
        for j in range(0,m):
            if [j+1,i+1] not in puddles:
                
                if n>i-1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if m>j-1>=0:
                    dp[i][j] += dp[i][j-1]
    
    return dp[n-1][m-1] % 1000000007