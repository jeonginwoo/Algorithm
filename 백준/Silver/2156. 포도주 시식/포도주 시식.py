import sys
input = sys.stdin.readline

n = int(input())
podoju = [int(input()) for _ in range(n)]

dp = [0] * n
dp[0] = podoju[0]
if n >= 2:
    dp[1] = podoju[0] + podoju[1]
if n >= 3:
    dp[2] = max(podoju[0], podoju[1]) + podoju[2]
    prevMaxNum = 0
    for i in range(3, n):
        prevMaxNum = max(prevMaxNum, dp[i-3])
        dp[i] = max(dp[i-2], prevMaxNum+podoju[i-1]) + podoju[i]

print(max(dp))