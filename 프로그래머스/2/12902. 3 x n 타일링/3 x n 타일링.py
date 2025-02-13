def solution(n):
    dp = [1] + [0]*(n//2)
    for i in range(1, n//2+1):
        dp[i] = dp[i-1]*3
    return dp[n//2] % 1000000007