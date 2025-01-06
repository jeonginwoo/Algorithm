import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
a, b = (K-1) // M, (K-1) % M

dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if K != 0 and ((i<a and j>b) or (i>a and j<b)):
            continue
        if i == 0 and j == 0:
            dp[i][j] = 1
        elif i == 0:
            dp[i][j] = dp[i][j-1]
        elif j == 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i][j-1] + dp[i-1][j]
            
print(dp[N-1][M-1])