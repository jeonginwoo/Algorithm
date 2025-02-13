def solution(n):
    dp = [1] + [0]*(n//2)
    stack = 0
    for i in range(1, n//2+1):
        stack += dp[i-2]*2
        dp[i] = dp[i-1]*3 + stack
    return dp[n//2] % 1000000007