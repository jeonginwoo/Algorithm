import sys
input = sys.stdin.readline

maxNum = 1000000
dp = [0]*(maxNum+1)
for i in range(1, maxNum+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i == 3:
        dp[i] = 4
    else:
        dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])