def solution(m, n, puddles):
    puddles = set(tuple(dot) for dot in puddles)
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        if (1, i+1) in puddles:
            break
        dp[i][0] = 1
    for j in range(m):
        if (j+1, 1) in puddles:
            break
        dp[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            if (j+1, i+1) in puddles:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for i in range(n):
        print(dp[i])

    return dp[-1][-1] % 1000000007